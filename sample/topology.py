'''
Created on Feb 21, 2016

@author: azaringh
'''

'''
Retrieve topology of the network
'''

import requests
requests.packages.urllib3.disable_warnings()
import json
import sys_constant as sc

url = "https://10.10.2.29:8443/oauth2/token"

payload = {'grant_type': 'password', 'username': sc.MY_USERNAME, 'password': sc.MY_PWD}
response = requests.post (url, data=payload, auth=(sc.MY_USERNAME,sc.MY_PWD), verify=False)
json_data = json.loads(response.text)
authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}

r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1', headers=authHeader, verify=False)
print json.dumps(r.json(), indent=4, separators=(',', ': '))
