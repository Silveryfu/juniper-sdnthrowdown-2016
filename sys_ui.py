import sys
import json
import sys_constant as sc
from sys_db_request import Controller_db
from sys_path_update import Lsp_update
from sys_ep_request import Ep_request
from sys_path_compute import Path_compute
from sys_link_event_handler import Link_event_handler
from pprint import pprint

class UI:
    def __init__(self, pc=Path_compute(), lu=Lsp_update(), leh = Link_event_handler()):
        self.running = True
        self.functions = {
            "change_link": self.change_link,
            "node_disjoint": self.node_disjoint,
            "link_disjoint": self.link_disjoint,
            "csp": self.constraint_shortest,
            "set_lsp": self.set_lsp,
            "exit": self.exit,
        }
        self.pc = pc
        self.lu = lu
        self.leh = leh

    def cui(self):
        print "SYS-V Console"
        while (self.running):
            cmd = raw_input(">> ")
            
            try:
                func = self.functions[cmd.split(" ")[0]]
                cmd_items = cmd.split(" '")[1:]
                for i in range(0, len(cmd_items)):
                    cmd_items[i] = cmd_items[i].replace("'", "")
                func(cmd_items)
            except:
                print "Input error!"
            '''
            func = self.functions[cmd.split(" ")[0]]
            cmd_items = cmd.split(" '")[1:]
            for i in range(0, len(cmd_items)):
                cmd_items[i] = cmd_items[i].replace("'", "")
            func(cmd_items)
            '''
    # cmd functions
    def exit(self, arg):
    # quit the console
        self.running = False

    # handle the topology change request issued by UI
    def handle (self, affect_lsp_list):

        link_lsp_map = self.lu.get_link_lsp_map()

        all_lsp_list = {}
        lsp_co_list = self.lu.get_lsps_by_node()
        for lsp_name in self.lu.get_lsp_name_list():
            if lsp_name.split("_")[1] == "ONE":
                all_lsp_list[lsp_name] = True

        text = ""
        print affect_lsp_list
        for lsp in all_lsp_list:
            number = int(lsp[-1])
            start = lsp.split('_')[2]
            if start == "SF":
                offset = 0
            else:
                offset = 4
            if lsp in affect_lsp_list:
                print "Re-arranged LSP ", lsp,
                if len(affect_lsp_list[lsp]) > 0:
                    print ":", affect_lsp_list[lsp]
                else:
                    print "no avaliable path found"
                lsp_co = []
                for node in affect_lsp_list[lsp]:
                    lsp_co.append(sc.node_co_map[sc.node_ip_map[node]])
                lsp_co_str = "lsp_" + bytes(number + offset) + "_path = " + json.dumps(lsp_co) + ";\n\n"
            else:
                lsp_co_str = "lsp_" + bytes(number + offset) + "_path = " + json.dumps(lsp_co_list[lsp]) + ";\n\n"
                #print lsp_co_str
            text = text + lsp_co_str
        with open("server_topo/lsp.js", "w") as f:
            f.write(text)
		
    def change_link(self, arg):
    # change the status (Up or down) of a link
    # endA: one end of the link, node name
    # endZ: another end of the link, node name
    # status: up or down
    # return: nothing
        if len(arg) != 3:
            print "Wrong number of argument (takes 3, %d given)"%len(arg)
            return
        (endA, endZ, new_status) = (arg[0], arg[1], arg[2])
        #print self.pc.compute(forged = (endA, endZ), status = new_status)
        status = { 
            "down": "failed",
            "up": "healed"
		}
        event = {
            "status": status[new_status],
            "interface_address": "forged"
        }
        self.leh.handle(event, forged_link = (endA, endZ), forged_status = new_status)

    def link_disjoint (self, arg):
    # set two link-disjoint lsp
    # lsp1: name of first lsp
    # lsp2: name of second lsp
        if len(arg) != 2:
            print "Wrong number of argument (takes 2, %d given)"%len(arg)
            return
        lsp1, lsp2 = arg[0], arg[1]
        lsp1_full, lsp2_full = 'GROUP_ONE_' + lsp1, 'GROUP_ONE_' + lsp2
        if lsp1.split("_")[0] == 'SF':
            node1, node2 = 'san francisco', 'new york'
        else:
            node2, node1 = 'san francisco', 'new york'
        affect_lsp_list = {}
        affect_lsp_list[lsp1_full], affect_lsp_list[lsp2_full] = self.pc.compute_link_disjoint_path(node1, node2)
        self.handle(affect_lsp_list)

    def node_disjoint (self, arg):
    # set two node-disjoint lsp
    # lsp1: name of first lsp
    # lsp2: name of second lsp
        if len(arg) != 2:
            print "Wrong number of argument (takes 2, %d given)"%len(arg)
            return
        lsp1, lsp2 = arg[0], arg[1]
        lsp1_full, lsp2_full = 'GROUP_ONE_' + lsp1, 'GROUP_ONE_' + lsp2
        if lsp1.split("_")[0] == 'SF':
            node1, node2 = 'san francisco', 'new york'
        else:
            node2, node1 = 'san francisco', 'new york'
        affect_lsp_list = {}
        affect_lsp_list[lsp1_full], affect_lsp_list[lsp2_full] = self.pc.compute_node_disjoint_path(node1, node2)
        self.handle(affect_lsp_list)
		
    def constraint_shortest (self, arg):
    # set a constraint shortest path
    # lsp: name of the lsp
    # bw: bandwidth constraint (float in MB)
        if len(arg) != 2:
            print "Wrong number of argument (takes 2, %d given)"%len(arg)
            return
        lsp, bw = arg[0], float(arg[1])
        lsp_full = 'GROUP_ONE_' + lsp
        if lsp.split("_")[0] == 'SF':
            node1, node2 = 'san francisco', 'new york'
        else:
            node2, node1 = 'san francisco', 'new york'
        affect_lsp_list = {}
        affect_lsp_list[lsp_full] = self.pc.compute_constrained_shortest_path(constraint=bw, node1=node1, node2=node2)
        self.handle(affect_lsp_list)

    def set_lsp(self, arg):
    # set an LSP to a certain path
    # lsp: name of an LSP
    # path: list of name of nodes along the lsp
        if len(arg) != 2:
            print "Wrong number of argument (takes 2, %d given)"%len(arg)
            return
        lsp_name, path_name = arg[0], arg[1]
        path = path_name.split(',')
        node_list = []
        for node in path:
            node_list.append(node)
        affect_lsp_list = {}
        affect_lsp_list[lsp_name] = node_list
        self.handle(affect_lsp_list)

if __name__ == "__main__":
    ui = UI()
    ui.cui()
