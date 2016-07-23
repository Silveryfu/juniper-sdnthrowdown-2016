'''
Created on July 21, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''
import requests
requests.packages.urllib3.disable_warnings()
import json

import sys_ep_request as ep
import sys_constant as sc

# class for updating the lsp
class Lsp_update:
    def __init__(self):
        self.er = ep.Ep_request()

    def get_all_links(self):
        # Get all the links (each indicated by a pair of nodes)
        # return: list of pairs of nodes -- the one with smaller IP suffix will be the 1st node in the pair
        link_list = self.er.ep_get_topo()['links']
        result_list = []
        for link in link_list:
            node_1 = sc.ip_node_map[link["endA"]["node"]["name"]]
            node_2 = sc.ip_node_map[link["endZ"]["node"]["name"]]
            result_list.append((node_1, node_2))
        return result_list

    def get_if_by_node(self, node_1, node_2):
        # Get interface_id by node name
        # node_1: start node name, string
        # node_2: end node name, string
        ip_1 = sc.node_ip_map[node_1]
        ip_2 = sc.node_ip_map[node_2]

        return self.get_if_by_node_ip(ip_1, ip_2)

    def get_if_by_node_ip(self, ip_1, ip_2):
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
            if_1, if_2 = self.get_if_by_node(node_list[i], node_list[i+1])
            update_ero.append({'topoObjectType': 'ipv4', 'address': if_2})

        # update the topology
        return self.er.ep_update_lsp_ero(lspName, ero = update_ero)

if __name__ == "__main__":
    Lu = Lsp_update()
    #print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP1", ['miami', 'dallas'])
    #print Lu.set_lsp_by_node("GROUP_ONE_SF_NY_LSP1", ['dallas', 'miami'])
    print Lu.set_lsp_by_node("GROUP_ONE_SF_NY_LSP4", ['dallas', 'miami'])
    #print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP2", [ 'miami', 'dallas', 'los angeles'])
    #print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP3", [ 'miami', 'dallas', 'los angeles'])
    #print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP4", [ 'miami', 'dallas', 'los angeles'])
    # print Lu.set_lsp_by_node("GROUP_ONE_NY_SF_LSP4", [ 'miami', 'dallas', 'los angeles'])
    # print Lu.get_all_links()
