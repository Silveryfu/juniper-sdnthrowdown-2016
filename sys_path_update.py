'''
Created on July 21, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''
import requests
requests.packages.urllib3.disable_warnings()
import json, socket

from pprint import pprint
from collections import defaultdict
from sys_ep_request import Ep_request
import sys_constant as sc

# class for updating the lsp
class Lsp_update:
    def __init__(self, er=Ep_request()):
        self.er = er

    def set_lsp_by_node(self, lspName, node_list):
        # Change the LSP by nodes
        # lspName: name of the LSP, string
        # node_list: list of nodes (names) along the LSP (no need to include SF or NY), [string]
        update_ero = []

        # in case the node_list has already included SF or NY
        direction = lspName.split('_')
        if node_list[0] != 'san francisco' and direction[-3] == 'SF':
            node_list.insert(0, 'san francisco')
        elif node_list[0] != 'new york' and direction[-3] == 'NY':
            node_list.insert(0, 'new york')
        if node_list[-1] != 'new york' and direction[-2] == 'NY':
            node_list.append('new york')
        elif node_list[-1] != 'san francisco' and direction[-2] == 'SF':
            node_list.append('san francisco')

        # generate ero
        for i in range(0, len(node_list)-1):
            if_1, if_2 = self.get_link_if_by_node(node_list[i], node_list[i+1])
            update_ero.append({'topoObjectType': 'ipv4', 'address': if_2})

        # update the topology
        return self.er.ep_update_lsp_ero(lspName, ero = update_ero)

    def get_link_if_by_node(self, node_1, node_2):
        # Get interface_id by node name
        # node_1: start node name, string
        # node_2: end node name, string
        ip_1 = sc.node_ip_map[node_1]
        ip_2 = sc.node_ip_map[node_2]

        return self.get_link_if_by_node_ip(ip_1, ip_2)

    def get_link_if_by_node_ip(self, ip_1, ip_2):
        # Get interface_id by node IP
        # ip_1: start node IP, string
        # ip_2: end node IP, string
        if int(ip_1.split('.')[-1]) > int(ip_2.split('.')[-1]):
            ip_endZ = ip_1
            ip_endA = ip_2
            reverse = True
        else:
            ip_endZ = ip_2
            ip_endA = ip_1
            reverse = False

        #self.er = ep.Ep_request()
        link_list = self.er.ep_get_topo()["links"]
        # with open("topology.txt", "w") as f:
        #     f.write(json.dumps(link_list, indent = 4))

        found = False
        for link in link_list:
            if link["endZ"]["node"]["name"] == ip_endZ and \
                            link["endA"]["node"]["name"] == ip_endA:
                if_1 = link["endA"]["ipv4Address"]["address"]
                if_2 = link["endZ"]["ipv4Address"]["address"]
                found = True
                break
        if not found:
            return "--> interface not found", "--> interface not found"
        if reverse:
            return if_2, if_1
        else:
            return if_1, if_2

    def get_all_link(self):
        # Get all the links (each indicated by a pair of nodes)
        # return: list of pairs of nodes -- the one with smaller IP suffix will be the 1st node in the pair
        link_list = self.er.ep_get_topo()['links']
        result_list = []
        for link in link_list:
            node_1 = sc.ip_node_map[link["endA"]["node"]["name"]]
            node_2 = sc.ip_node_map[link["endZ"]["node"]["name"]]
            if int(link["endA"]["node"]["name"].split('.')[-1]) < int(link["endZ"]["node"]["name"].split('.')[-1]):
                result_list.append((node_1, node_2))
            else:
                result_list.append((node_2, node_1))
        return result_list

    def get_link_status(self, link):
        link_name = sc.node_link_map[link]
        link_list = self.er.ep_get_topo()['links']
        for link in link_list:
            if link["name"] == link_name:
                return link["operationalStatus"]
        return "Down"

    def get_lsp_name_list(self):
        # return: list of lsp names, list
        lsp_list = []
        for lsp in self.er.ep_get_lsp_list():
            lsp_list.append(lsp['name'].encode('ascii'))
        return lsp_list

    def get_if_link_map(self):
        # return: {if_address: link_name}
        if_link_dict = {}

        for link in self.er.ep_get_topo()['links']:
            temp = link['name'].lstrip('L')
            temp = temp.split('_')
            if_1 = temp[0]
            if_2 = temp[1]
            if_link_dict[if_1] = link['name']
            if_link_dict[if_2] = link['name']
        return if_link_dict

    def get_link_node_map(self):
        link_node_dict = {}
        for link in self.er.ep_get_topo()['links']:
            node_1 = link['endA']['node']['name']
            node_2 = link['endZ']['node']['name']
            link_node_dict[link['name']] = (node_1, node_2)
        return link_node_dict

    def get_if_node_map(self):
        if_node_dict = {}
        for router in sc.routers:
            if_list = router['interfaces']
            for interface in if_list:
                if_node_dict[interface['address']] = router['router_id']
        return if_node_dict

    def get_link_lsp_map(self):
        link_lsp_dict = defaultdict(list)
        for lsp in self.er.ep_get_lsp_list():
            lsp_name = lsp['name']
            try:
                ero = lsp['liveProperties']['ero']
            except KeyError:
                continue

            for node in ero:
                address = node['address']
                try:
                    socket.inet_aton(address)
                    link_lsp_dict[sc.if_link_map[address]].append(lsp_name)
                except socket.error:
                    pass
        return link_lsp_dict

    def dump_lsp_path(self, lspName = None):
        path_list = {}
        #with open ("debug.txt", "w") as f:
        #    f.write(json.dumps(self.er.ep_get_lsp_list(), indent = 4))
        for lsp in self.er.ep_get_lsp_list():
            lsp_name = lsp['name']
            if sc.GROUP_ID not in lsp_name:
                continue
            if lspName != None and lsp_name != lspName:
                continue
            path = []
            if lsp['name'].split("_")[2] == "SF":
                path.append(sc.node_ip_map['san francisco'])
            elif lsp['name'].split("_")[2] == "NY":
                path.append(sc.node_ip_map['new york'])
            try:
                ero = lsp['liveProperties']['ero']
            except KeyError:
                continue

            for node in ero:
                address = node['address']
                try:
                    socket.inet_aton(address)
                    path.append(sc.if_node_map[address])
                except socket.error:
                    path.append(sc.node_ip_map[address])
                    pass
            # MANUALLY check if the end point of an lSP path is the REAL end point (some how the REST API doesn't do it consistantly on this!)
            if lsp['name'].split("_")[3] == "NY" and sc.ip_node_map[path[-1]] != 'new york':
                path.append(sc.node_ip_map['new york'])
            elif lsp['name'].split("_")[3] == "SF" and sc.ip_node_map[path[-1]] != 'san francisco':
                path.append(sc.node_ip_map['san francisco'])            
            path_list[lsp_name] = path
        return path_list

    def get_lsps_by_node(self):
        lsps = self.dump_lsp_path()
        lsp_list = {}
        for lsp in lsps:
            lsp_co = []
            for node in lsps[lsp]:
                lsp_co.append(sc.node_co_map[node])
            lsp_list[lsp] = lsp_co
        return lsp_list

    def get_lsp_by_name(self, lspName):
        path_list = self.dump_lsp_path(lspName = lspName)[0]
        name_list = []
        for ip in path_list:
	        name_list.append(sc.ip_node_map[ip])
        return name_list
			
if __name__ == "__main__":
    Lu = Lsp_update()
    # print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP1", ['miami', 'tampa', 'houston', 'dallas', 'los angeles'])
    #print Lu.dump_lsp_path('GROUP-SEVEN_SF_NY_LSP4')
    # Lu.get_link_lsp_map()
    #print Lu.get_lsp_name_list()
    #print Lu.set_lsp_by_node("GROUP_ONE_SF_NY_LSP1", ['dallas', 'miami'])
    #pprint(Lu.get_all_links())
    #print Lu.set_lsp_by_node("GROUP_ONE_SF_NY_LSP4", ['dallas', 'miami'])
    #print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP2", [ 'miami', 'dallas', 'los angeles'])
    #print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP3", [ 'miami', 'dallas', 'los angeles'])
    #print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP4", [ 'miami', 'dallas', 'los angeles'])
    #print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP4", [ 'miami', 'dallas', 'los angeles'])
    #print Lu.get_all_links()
    #print Lu.get_link_status(("10.210.15.1", "10.210.15.2"))
    #pprint (Lu.get_lsp_name_list())
    #print Lu.get_lsp_by_name('GROUP_ONE_SF_NY_LSP4')
    #print Lu.get_lsps_by_node()
    #pprint(Lu.get_all_link())
    #pprint(Lu.get_lsps_by_node())
    print Lu.set_lsp_by_node("GROUP_ONE_SF_NY_LSP1", ['dallas', 'houston', 'tampa'])
    print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP1", ['chicago', 'dallas'])
