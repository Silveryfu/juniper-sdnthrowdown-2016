'''
Created on July 24, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''
import requests
requests.packages.urllib3.disable_warnings()
import sys_constant as sc
from pprint import pprint
import json
import time
import random
import threading


from sys_path_update import Lsp_update

class Demo_Mgr(threading.Thread):
    def __init__(self, lu=Lsp_update()):
        threading.Thread.__init__(self)
        self.lu = lu
        self.lsp_ind = 1
        self.go = True

    def run(self):
        while (self.go):
            temp = random.randint (1, 8)
            while (self.lsp_ind == temp):
                temp = random.randint (1, 8)
            self.lsp_ind = temp          
            self.update_lsp_data()
            time.sleep(60)

    def update_lsp_data(self):
        lsp_co_list = self.lu.get_lsps_by_node()
        with open("server_topo/lsp.js", "w") as f:
            for lsp_co in lsp_co_list:
                lsp_co_str = "lsp_" + bytes(self.lsp_ind%8 + 1) + "_path = " + json.dumps(lsp_co_list[lsp_co]) + ";\n\n"
                f.write(lsp_co_str)
                self.lsp_ind = (self.lsp_ind + 1)%8


if __name__ == "__main__":
    try:
        dm = Demo_Mgr()
        dm.daemon=True
        dm.start()
        time.sleep(100)
    except KeyboardInterrupt:
        print "Stopped."