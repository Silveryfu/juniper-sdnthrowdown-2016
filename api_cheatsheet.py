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
        url = "https://10.10.2.29:8443/oauth2/token"
        payload = {'grant_type': 'password', 'username': sc.MY_USERNAME, 'password': sc.MY_PWD}
        response = requests.post(url, data=payload, auth=(sc.MY_USERNAME, sc.MY_PWD), verify=False)
        json_data = json.loads(response.text)
        self.authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}

        self.ep_lsp = 'https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/'
        self.ep_topo = 'https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1'
        self.ep_link = 'https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/links/'
        self.ep_node = 'https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/nodes/'

    def ep_read(self, ep=None):
        r = requests.get(ep, headers=self.authHeader, verify=False)
        return json.loads(json.dumps(r.json()))

    def ep_write(self, ep=None):
        pass

    def ep_update_lsp(self, lsp_name, ero=sc.default_ero):
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

        return requests.put('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/' + str(lsp_new['lspIndex']),
                                json=lsp_new, headers=self.authHeader, verify=False)

if __name__ == "__main__":
    er = Ep_request()
    response = er.ep_update_lsp('GROUP_ONE_SF_NY_LSP1')
    if isinstance(response, str):
        print response
    else:
        pprint.pprint(response.text)


