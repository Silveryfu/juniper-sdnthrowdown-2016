'''
Created on July 25, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''
import redis
import json
import time
import threading
import sys_constant as sc
from pprint import pprint
from sys_path_compute import Path_compute
from sys_path_update import Lsp_update
from sys_db_request import Controller_db

class Link_monitor (threading.Thread):
    def __init__(self, lu=Lsp_update(), cd=Controller_db.from_new_redis()):
        threading.Thread.__init__(self)
        self.lu = lu
        self.cd = cd
        self.running = True

    def run(self):
        print '[link monitor]: started ...'
        while(self.running):
            self.update_all_link_data()
            print 'link updated'
            time.sleep(10)
    
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

if __name__ == "__main__":
    while(True):
        try:
            Lm = Link_monitor()
            Lm.daemon=True
            Lm.start()
            time.sleep(100)
        except KeyboardInterrupt:
            print "Stopped."
            break
