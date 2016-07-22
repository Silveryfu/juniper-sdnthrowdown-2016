MY_USERNAME = 'group1'
MY_PWD = 'Group1'

TOKEN_URI = "https://10.10.2.29:8443/oauth2/token"
CONTROLLER_URI = 'https://10.10.2.29:8443/NorthStar/API/'
CONTROLLER_DB_URI = '10.10.4.252'
CONTROLLER_DB_PORT = 6379
CONTROLLER_DB_NUM = 0
API_VERSION = 'v1'
TENANT_ID = '1'
TOPO_ID = '1'

TOPO_EP = CONTROLLER_URI + API_VERSION + '/tenant/' + TENANT_ID + '/topology/' + TOPO_ID + '/'

default_ero = [
                { 'topoObjectType': 'ipv4', 'address': '10.210.15.2'},
                { 'topoObjectType': 'ipv4', 'address': '10.210.13.2'},
                { 'topoObjectType': 'ipv4', 'address': '10.210.17.1'}
               ]

routers = [
           { 'name': 'chicago', 'router_id': '10.210.10.124', 'interfaces': [
                                                                            { 'name': 'ge-1/0/1', 'address': '10.210.16.2' },
                                                                            { 'name': 'ge-1/0/2', 'address': '10.210.13.2' },
                                                                            { 'name': 'ge-1/0/3', 'address': '10.210.14.2' },
                                                                            { 'name': 'ge-1/0/4', 'address': '10.210.17.2' }
                                                                            ]
            },
           { 'name': 'san francisco', 'router_id': '10.210.10.100', 'interfaces': [
                                                                            { 'name': 'ge-1/0/0', 'address': '10.210.18.1' },
                                                                            { 'name': 'ge-1/0/1', 'address': '10.210.15.1' },
                                                                            { 'name': 'ge-1/0/3', 'address': '10.210.16.1' }
                                                                            ]
            },
           { 'name': 'dallas', 'router_id': '10.210.10.106', 'interfaces': [
                                                                             { 'name': 'ge-1/0/0', 'address': '10.210.15.2' },
                                                                             { 'name': 'ge-1/0/1', 'address': '10.210.19.1' },
                                                                             { 'name': 'ge-1/0/2', 'address': '10.210.21.1' },
                                                                             { 'name': 'ge-1/0/3', 'address': '10.210.11.1' },
                                                                             { 'name': 'ge-1/0/4', 'address': '10.210.13.1' }
                                                                             ]
            },
           { 'name': 'miami', 'router_id': '10.210.10.112', 'interfaces': [
                                                                            { 'name': 'ge-1/0/0', 'address': '10.210.22.1' },
                                                                            { 'name': 'ge-1/0/1', 'address': '10.210.24.1' },
                                                                            { 'name': 'ge-1/0/2', 'address': '10.210.12.1' },
                                                                            { 'name': 'ge-1/0/3', 'address': '10.210.11.2' },
                                                                            { 'name': 'ge-1/0/4', 'address': '10.210.14.1' }
                                                                            ]
            },
           { 'name': 'new york', 'router_id': '10.210.10.118', 'interfaces': [
                                                                               { 'name': 'ge-1/0/3', 'address': '10.210.12.2' },
                                                                               { 'name': 'ge-1/0/5', 'address': '10.210.17.1' },
                                                                               { 'name': 'ge-1/0/7', 'address': '10.210.26.1' }
                                                                               ]
            },
           { 'name': 'los angeles', 'router_id': '10.210.10.113', 'interfaces': [
                                                                                  { 'name': 'ge-1/0/0', 'address': '10.210.18.2' },
                                                                                  { 'name': 'ge-1/0/1', 'address': '10.210.19.2' },
                                                                                  { 'name': 'ge-1/0/2', 'address': '10.210.20.1' }
                                                                                  ]
            },
           { 'name': 'houston', 'router_id': '10.210.10.114', 'interfaces': [
                                                                              { 'name': 'ge-1/0/0', 'address': '10.210.20.2' },
                                                                              { 'name': 'ge-1/0/1', 'address': '10.210.21.2' },
                                                                              { 'name': 'ge-1/0/2', 'address': '10.210.22.2' },
                                                                              { 'name': 'ge-1/0/3', 'address': '10.210.25.1' }
                                                                              ]
            },
           { 'name': 'tampa', 'router_id': '10.210.10.115', 'interfaces': [
                                                                            { 'name': 'ge-1/0/0', 'address': '10.210.25.2' },
                                                                            { 'name': 'ge-1/0/1', 'address': '10.210.24.2' },
                                                                            { 'name': 'ge-1/0/2', 'address': '10.210.26.2' }
                                                                            ]
            }
           ]


