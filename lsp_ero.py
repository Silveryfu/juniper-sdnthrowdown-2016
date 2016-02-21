'''
Created on Feb 21, 2016

@author: azaringh
'''
import requests
requests.packages.urllib3.disable_warnings()
import json

url = "https://10.10.2.25:8443/oauth2/token"

payload = {'grant_type': 'password', 'username': 'some_name', 'password': 'some_password'}
response = requests.post (url, data=payload, auth=('some_name','some_password'), verify=False)
json_data = json.loads(response.text)
authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}

r = requests.get('https://10.10.2.25:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/', headers=authHeader, verify=False)

p = json.dumps(r.json())
lsp_list = json.loads(p)
# Find target LSP to use lspIndex
for lsp in lsp_list:
    if lsp['name'] == 'GROUP_FIVE_SF_NY_LSP3':
        break

# Fill only the required fields     
ero= [ 
                { 'topoObjectType': 'ipv4', 'address': '10.210.15.2'},
                { 'topoObjectType': 'ipv4', 'address': '10.210.13.2'},
                { 'topoObjectType': 'ipv4', 'address': '10.210.17.1'}
               ]
new_lsp = {}
for key in ('from', 'to', 'name', 'lspIndex', 'pathType'):
    new_lsp[key] = lsp[key]

new_lsp['plannedProperties'] = {
    'ero': ero
}

response = requests.put('https://10.10.2.25:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/' + str(new_lsp['lspIndex']), 
                        json = new_lsp, headers=authHeader, verify=False)
print response.text
