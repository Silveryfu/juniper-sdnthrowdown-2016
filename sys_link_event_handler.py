'''
Created on July 22, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''

import redis
import json
import threading
import sys_constant as sc
from pprint import pprint
from sys_path_compute import Path_compute
from sys_path_update import Lsp_update
from sys_db_request import Controller_db


class Link_event_handler(threading.Thread):
    def __init__(self, r=redis.StrictRedis(host=sc.CONTROLLER_DB_URI,
                                           port=sc.CONTROLLER_DB_PORT,
                                           db=sc.CONTROLLER_DB_NUM),
                 pc=Path_compute(), lu=Lsp_update(), cd=Controller_db.from_new_redis()):
        threading.Thread.__init__(self)

        self.pc = pc
        self.lu = lu
        self.redis = r
        self.cd = cd
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe('link_event')

        self.topo = {}
        self.lsp_list = []

        # only manage lsp owned
        for lsp_name in self.lu.get_lsp_name_list():
            if sc.GROUP_ID in lsp_name:
                self.lsp_list.append(lsp_name)

    def run(self):
        for item in self.pubsub.listen():
            print item['channel'], ":", item['data']
            if isinstance(item['data'], basestring):
                event = json.loads(item['data'])
                self.handle(event)

    def handle(self, event, forged_link = None, forged_status = None):
        status = event["status"]
        link_lsp_map = self.lu.get_link_lsp_map()
        if forged_link == None:
            affect_link = sc.if_link_map[event["interface_address"]]
        else:
            ip_1 = sc.node_ip_map[forged_link[0]]
            ip_2 = sc.node_ip_map[forged_link[1]]
            if int(ip_1.split('.')[-1]) < int(ip_2.split('.')[-1]):
                (IP_endA, IP_endZ) = (ip_1, ip_2)
            else:
                forged_link = (forged_link[1], forged_link[0])
                (IP_endA, IP_endZ) = (ip_2, ip_1)
            affect_link = sc.node_link_map[(IP_endA, IP_endZ)]
        affect_lsp_list = {}
        for item in link_lsp_map[affect_link]:
            affect_lsp_list[item] = True
        all_lsp_list = {}
        lsp_co_list = self.lu.get_lsps_by_node()
        for lsp_name in self.lu.get_lsp_name_list():
            if lsp_name.split("_")[1] == "ONE":
                all_lsp_list[lsp_name] = True
        if (event['status'] == "healed" or forged_status == "healed"):
            affect_lsp_list = all_lsp_list
        else:
            text = ""
            for lsp in all_lsp_list:
                number = int(lsp[-1])
                start = lsp.split('_')[2]
                if start == "SF":
                    offset = 0
                else:
                    offset = 4
                if lsp in affect_lsp_list:
                    lsp_co_str = "lsp_" + bytes(number + offset) + "_path = " + json.dumps({}) + ";\n\n"
                else:
                    lsp_co_str = "lsp_" + bytes(number + offset) + "_path = " + json.dumps(lsp_co_list[lsp]) + ";\n\n"
                text = text + lsp_co_str
            with open("server_topo/lsp.js", "w") as f:
                f.write(text)

        print "event: link", event['status']
        print "affected link: ", affect_link
        #print "affect lsp list:"
        #print affect_lsp_list
		
        (endA_IP, endZ_IP) = sc.link_node_map[affect_link]
        (endA_co, endZ_co) = (sc.node_co_map[endA_IP], sc.node_co_map[endZ_IP])

        # write the affected link to the file server_topo/link_event.js
        with open("server_topo/link_event.js", "w") as f:
            event_str = "link_event = " + json.dumps([endA_co, endZ_co, {"status": status}]) + ";\n\n"
            f.write(event_str)

        # get the adjacent list once for all
        #self.pc.get__adjacent_list(forged = forged_link, status = forged_status);
        solved = {}
        for lsp_name in affect_lsp_list:
            if sc.GROUP_ID not in lsp_name:
                continue
            else:
                self.pc.get__adjacent_list(forged = forged_link, status = forged_status);
                new_path = self.pc.compute()
                if lsp_name.split('_')[2] == 'NY':
                    new_path = list(reversed(new_path))
                #print self.lu.get_lsp_by_name(lsp_name)
                print "Re-arranged LSP ", lsp_name,
                print ":", new_path
                self.lu.set_lsp_by_node(lsp_name, new_path)
                solved[lsp_name] = True
            lsp_path = []
            for node in new_path:
                lsp_path.append(sc.node_co_map[sc.node_ip_map[node]])
            lsp_co_list[lsp_name] = lsp_path
            #print lsp_co_list
            with open("server_topo/lsp.js", "w") as f:
                for lsp_co in lsp_co_list:
                    number = int(lsp_co[-1])
                    start = lsp_co.split('_')[2]
                    if start == "SF":
                        offset = 0
                    else:
                        offset = 4
                    if lsp_co in affect_lsp_list and not lsp_co in solved:
                        lsp_co_str = "lsp_" + bytes(number + offset) + "_path = " + json.dumps({}) + ";\n\n"
                    else:
                        lsp_co_str = "lsp_" + bytes(number + offset) + "_path = " + json.dumps(lsp_co_list[lsp_co]) + ";\n\n"
                    f.write(lsp_co_str)

    def update_all_link_data(self):
    # update the whole link data and write it into server_topo/link.js
        link_list = self.lu.get_all_link()
        with open("server_topo/link.js", "w") as f:
            ind = 1
            for link in link_list:
                endA_IP = sc.node_ip_map[link[0]]
                endZ_IP = sc.node_ip_map[link[1]]
                bandwidth = self.cd.get_link_bw(link[0], link[1])
                link_json = [sc.node_co_map[endA_IP], sc.node_co_map[endZ_IP], {"status": self.lu.get_link_status((endA_IP, endZ_IP)), "bandwidth":bandwidth}]
                link_str = "link_" + bytes(ind) + " = " + json.dumps(link_json, indent = 4) + ";\n\n"
                ind += 1
                f.write(link_str)
        
    def update_lsp(self):
        pass

if __name__ == "__main__":
    handler = Link_event_handler()
    #handler.start()
    handler.handle({"status":"failed", "interface_address":"10.210.16.1"})
    #handler.handle(sc.test_fail_event)
