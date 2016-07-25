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


class Link_event_handler(threading.Thread):
    def __init__(self, r=redis.StrictRedis(host=sc.CONTROLLER_DB_URI,
                                           port=sc.CONTROLLER_DB_PORT,
                                           db=sc.CONTROLLER_DB_NUM),
                 pc=Path_compute(), lu=Lsp_update()):
        threading.Thread.__init__(self)

        self.pc = pc
        self.lu = lu
        self.redis = r
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
                self.update_topo(event)
                self.handle(event)

    def handle(self, event):
        status = event["status"]
        link_lsp_map = self.lu.get_link_lsp_map()
        affect_link = sc.if_link_map[event["interface_address"]]
        affect_lsp_list = link_lsp_map[affect_link]
        print event
        print affect_link
		
        (endA_IP, endZ_IP) = sc.link_node_map[affect_link]
        (endA_co, endZ_co) = (sc.node_co_map[endA_IP], sc.node_co_map[endZ_IP])

        # write the affected link to the file server_topo/link_event.js
        with open("server_topo/link_event.js", "w") as f:
            event_str = "link_event = " + json.dumps([endA_co, endZ_co, {"status": status}]) + ";\n\n"
            f.write(event_str)
		
        for lsp_name in affect_lsp_list:
            if sc.GROUP_ID not in lsp_name:
                continue
            else:
                new_path = self.pc.compute()
                self.lu.set_lsp_by_node(lsp_name, new_path)

    def update_all_link_data(self):
    # update the whole link data and write it into server_topo/link.js
        link_list = self.lu.get_all_link()
        with open("server_topo/link.js", "w") as f:
            ind = 1
            for link in link_list:
                endA_IP = sc.node_ip_map[link[0]]
                endZ_IP = sc.node_ip_map[link[1]]
                link_json = [sc.node_co_map[endA_IP], sc.node_co_map[endZ_IP], {"status": self.lu.get_link_status((endA_IP, endZ_IP))}]
                link_str = "link_" + bytes(ind) + " = " + json.dumps(link_json, indent = 4) + ";\n\n"
                ind += 1
                f.write(link_str)
        
    def update_topo(self):
        pass

if __name__ == "__main__":
    handler = Link_event_handler()
    #handler.start()
    handler.handle({"status":"failed", "interface_address":"10.210.18.1"})
    # handler.handle(sc.test_fail_event)
