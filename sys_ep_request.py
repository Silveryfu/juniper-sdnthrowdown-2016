'''
Created on July 21, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''
import requests
requests.packages.urllib3.disable_warnings()
import sys_constant as sc
from pprint import pprint
import json

class Ep_request:
    def __init__(self):
        payload = {'grant_type': 'password', 'username': sc.MY_USERNAME, 'password': sc.MY_PWD}
        response = requests.post(sc.TOKEN_URI, data=payload, auth=(sc.MY_USERNAME, sc.MY_PWD), verify=False)
        json_data = json.loads(response.text)
        self.authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}

        self.ep_topo = sc.TOPO_EP
        self.ep_link = sc.TOPO_EP + 'links/'
        self.ep_node = sc.TOPO_EP + 'nodes/'
        self.ep_lsp = sc.TOPO_EP + 'te-lsps/'

    def ep_get_node_location(self, node_id):
        p = json.dumps(self.ep_get_node())
        nodes = json.loads(p)

        for node in nodes:
            if node['name'] == node_id:
                print node['name'], ':'
                print '\t latitude: ', node['topology']['coordinates']['coordinates'][0]
                print '\t longitude: ', node['topology']['coordinates']['coordinates'][1]
                break

    def ep_update_lsp_ero(self, lsp_name, ero=sc.default_ero):
        # End point call to update the ero given lsp name
        # lsp_name: string
        # ero: new ero, list
        lsp_list, lsp_new = self.ep_read(self.ep_lsp), None

        is_match=False
        for lsp in lsp_list:
            if lsp['name'] == lsp_name:
                is_match=True
                break

        if not is_match:
            return "--> Non-existent LSP or invalid name."

        lsp_new = {}
        for key in ('from', 'to', 'name', 'lspIndex', 'pathType'):
            lsp_new[key] = lsp[key]

        lsp_new['plannedProperties'] = {
            'ero': ero
        }

        return requests.put(self.ep_lsp + str(lsp_new['lspIndex']),
                            json=lsp_new, headers=self.authHeader, verify=False)

    def ep_read(self, ep):
        # End point call for the given end point uri
        # ep: string
        return json.loads(json.dumps(requests.get(ep, headers=self.authHeader, verify=False).json()))

    def ep_get_lsp_by_id(self, id):
        return self.ep_read(self.ep_lsp + id)

    def ep_get_lsp(self, lsp_name):
        # End point call for lsp
        # lsp_name: name of the target lsp, string
        id = self.ep_name_to_id(lsp_name)
        if id is None:
            return "--> Non-existent LSP or invalid name."
        return self.ep_read(self.ep_lsp + id)

    def ep_lsp_name_to_id(self, lsp_name):
        # End point call for mapping lsp name to index
        # lsp_name: name of the target lsp, string
        id = None
        for lsp in self.ep_read(self.ep_lsp):
            if lsp['name'] == lsp_name:
                id = lsp['lspIndex']
        return str(id)

    def ep_get_topo(self):
        return self.ep_read(self.ep_topo)

    def ep_get_node(self):
        return self.ep_read(self.ep_node)

    def ep_get_lsp_list(self):
        #return self.ep_read(self.ep_lsp)
        p = self.ep_read(self.ep_lsp)
        #pprint (p)
        '''
        with open("debug.txt","w") as f:
            f.write(json.dumps(p,indent = 4))
        '''
        return p


if __name__ == "__main__":
    er = Ep_request()
    #er.ep_get_node_location('10.210.10.124')
    print er.ep_get_lsp_list()




