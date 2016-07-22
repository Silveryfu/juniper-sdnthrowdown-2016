'''
Created on July 21, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''
import requests
requests.packages.urllib3.disable_warnings()
import json
import pprint
import sys_constant as sc

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

    def ep_update_lsp_ero(self, lsp_name, ero=sc.default_ero):
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
        r = requests.get(ep, headers=self.authHeader, verify=False)
        return json.loads(json.dumps(r.json()))

    def ep_read_lsp_by_id(self, id):
        return self.ep_read(self.ep_lsp + id)

    def ep_read_lsp_by_name(self, lsp_name):
        id = self.ep_name_to_id(lsp_name)
        if id is None:
            return "--> Non-existent LSP or invalid name."
        return self.ep_read(self.ep_lsp + id)

    def ep_lsp_name_to_id(self, lsp_name):
        lsp_list = self.ep_read(self.ep_lsp)
        id = None
        for lsp in lsp_list:
            if lsp['name'] == lsp_name:
                id = lsp['lspIndex']
        return str(id)

    def ep_get_link(self, node_1=None, node_2=None):
        topo = self.ep_read(self.ep_topo)
        pprint.pprint(topo)
        pass

if __name__ == "__main__":
    er = Ep_request()
    er.ep_get_link()





