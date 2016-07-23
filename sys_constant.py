MY_USERNAME = 'group1'
MY_PWD = 'Group1'

TOKEN_URI = "https://10.10.2.29:8443/oauth2/token"
CONTROLLER_URI = 'https://10.10.2.29:8443/NorthStar/API/'
CONTROLLER_DB_URI = '10.10.4.252'
CONTROLLER_DB_PORT = 6379
CONTROLLER_DB_NUM = 0

VM_EAST = '10.10.2.200'
VM_WEST = '10.10.2.220'
INFLUX_PORT = 8086
INFLUX_USER = 'root'
INFLUX_PASSWORD = 'root'
INFLUX_NAME = 'analytics'

API_VERSION = 'v1'
TENANT_ID = '1'
TOPO_ID = '1'
TOPO_SERVER_PORT = 8081

TOPO_EP = CONTROLLER_URI + API_VERSION + '/tenant/' + TENANT_ID + '/topology/' + TOPO_ID + '/'

default_ero = [
                { 'topoObjectType': 'ipv4', 'address': '10.210.15.2'},
                { 'topoObjectType': 'ipv4', 'address': '10.210.13.2'},
                { 'topoObjectType': 'ipv4', 'address': '10.210.17.1'}
               ]

routers = [{'interfaces': 
                [{'address': '10.210.16.2', 'name': 'ge-1/0/1'},
                 {'address': '10.210.13.2', 'name': 'ge-1/0/2'},
                 {'address': '10.210.14.2', 'name': 'ge-1/0/3'},
                 {'address': '10.210.17.2', 'name': 'ge-1/0/4'}],
                  'latitude': 41.84,
                  'longitude': -87.68,
                  'name': 'chicago',
                  'router_id': '10.210.10.124'},

           {'interfaces': [{'address': '10.210.18.1', 'name': 'ge-1/0/0'},
                           {'address': '10.210.15.1', 'name': 'ge-1/0/1'},
                           {'address': '10.210.16.1', 'name': 'ge-1/0/3'}],
                  'latitude': 37.79,
                  'longitude': -122.55,
                  'name': 'san francisco',
                  'router_id': '10.210.10.100'},

           {'interfaces': [{'address': '10.210.15.2', 'name': 'ge-1/0/0'},
                           {'address': '10.210.19.1', 'name': 'ge-1/0/1'},
                           {'address': '10.210.21.1', 'name': 'ge-1/0/2'},
                           {'address': '10.210.11.1', 'name': 'ge-1/0/3'},
                           {'address': '10.210.13.1', 'name': 'ge-1/0/4'}],
                  'latitude': 32.789997,
                  'longitude': -96.77,
                  'name': 'dallas',
                  'router_id': '10.210.10.106'},

           {'interfaces': [{'address': '10.210.22.1', 'name': 'ge-1/0/0'},
                           {'address': '10.210.24.1', 'name': 'ge-1/0/1'},
                           {'address': '10.210.12.1', 'name': 'ge-1/0/2'},
                           {'address': '10.210.11.2', 'name': 'ge-1/0/3'},
                           {'address': '10.210.14.1', 'name': 'ge-1/0/4'}],
                  'latitude': 25.78,
                  'longitude': -80.21,
                  'name': 'miami',
                  'router_id': '10.210.10.112'},

           {'interfaces': [{'address': '10.210.12.2', 'name': 'ge-1/0/3'},
                           {'address': '10.210.17.1', 'name': 'ge-1/0/5'},
                           {'address': '10.210.26.1', 'name': 'ge-1/0/7'}],
                  'latitude': 40.67,
                  'longitude': -73.94,
                  'name': 'new york',
                  'router_id': '10.210.10.118'},

           {'interfaces': [{'address': '10.210.18.2', 'name': 'ge-1/0/0'},
                           {'address': '10.210.19.2', 'name': 'ge-1/0/1'},
                           {'address': '10.210.20.1', 'name': 'ge-1/0/2'}],
                  'latitude': 34.11,
                  'longitude': -118.41,
                  'name': 'los angeles',
                  'router_id': '10.210.10.113'},

           {'interfaces': [{'address': '10.210.20.2', 'name': 'ge-1/0/0'},
                           {'address': '10.210.21.2', 'name': 'ge-1/0/1'},
                           {'address': '10.210.22.2', 'name': 'ge-1/0/2'},
                           {'address': '10.210.25.1', 'name': 'ge-1/0/3'}],
                  'latitude': 29.770002,
                  'longitude': -95.39,
                  'name': 'houston',
                  'router_id': '10.210.10.114'},

           {'interfaces': [{'address': '10.210.25.2', 'name': 'ge-1/0/0'},
                           {'address': '10.210.24.2', 'name': 'ge-1/0/1'},
                           {'address': '10.210.26.2', 'name': 'ge-1/0/2'}],
                  'latitude': 27.960001,
                  'longitude': -82.48,
                  'name': 'tampa',
                  'router_id': '10.210.10.115'}]

node_ip_map = {
    'san francisco': '10.210.10.100',
	'dallas'       : '10.210.10.106',
	'miami'        : '10.210.10.112',
	'los angeles'  : '10.210.10.113',
	'houston'      : '10.210.10.114',
	'tampa'        : '10.210.10.115',
	'new york'     : '10.210.10.118',
	'chicago'      : '10.210.10.124'
}

ip_node_map = {
    '10.210.10.100': 'san francisco',
	'10.210.10.106': 'dallas',
	'10.210.10.112': 'miami',
	'10.210.10.113': 'los angeles',
	'10.210.10.114': 'houston',
	'10.210.10.115': 'tampa',
	'10.210.10.118': 'new york',
	'10.210.10.124': 'chicago'
}
