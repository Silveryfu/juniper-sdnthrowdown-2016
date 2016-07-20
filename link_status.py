'''
Created on Feb 21, 2016

@author: azaringh
'''
import requests
requests.packages.urllib3.disable_warnings()
import json
import pprint
import sys_constant as sc

routers = sc.routers

url = "https://10.10.2.25:8443/oauth2/token"

payload = {'grant_type': 'password', 'username': sc.MY_USERNAME, 'password': sc.MY_PWD}
response = requests.post (url, data=payload, auth=(sc.MY_USERNAME,sc.MY_PWD), verify=False)
json_data = json.loads(response.text)
authHeader= {"Authorization":"{token_type} {access_token}".format(**json_data)}

r = requests.get('https://10.10.2.25:8443/NorthStar/API/v1/tenant/1/topology/1/links/', headers=authHeader, verify=False)

p = json.dumps(r.json())
links = json.loads(p)
print links[0]['operationalStatus']

flag = False
aNodeName = ''
zNodeName = ''
aLinkName = ''
zLinkName = ''
for link in links:
    if link['operationalStatus'] == 'Up':
        continue
    flag = True
    pprint.pprint(link)
    for r in routers:
        if r['router_id'] == link['endA']['node']['name']:
            aNodeName = r['name']
            for i in r['interfaces']:
                if i['address'] == link['endA']['ipv4Address']['address']:
                    aLinkName = i['name']
        if r['router_id'] == link['endZ']['node']['name']:
            zNodeName = r['name']
            for i in r['interfaces']:
                if i['address'] == link['endZ']['ipv4Address']['address']:
                    zLinkName = i['name']                    
                     
if flag == True:
    print 'Link failure:'
    print '\tA: ', aNodeName, aLinkName
    print '\tZ: ', zNodeName, zLinkName
else:
    print "All links Up"

