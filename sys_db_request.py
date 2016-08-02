'''
Created on July 21, 2016

All data observes to format:
(timestamp, data_entry_1, ..., data_entry_n, unit)
e.g., (u'Sat:00:41:32', u'0', u'1856', 'bps')

One method should return only one type of data.

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''

import sys_constant as sc
import redis
import json
from influxdb import InfluxDBClient
from pprint import pprint
import sys_path_update as spu   

class Controller_db:
    def __init__(self, r):
        self.redis = r
        self.influx = None

    @classmethod
    def from_new_redis(cls):
        return cls(redis.StrictRedis(host=sc.CONTROLLER_DB_URI,
                                         port=sc.CONTROLLER_DB_PORT,
                                         db=sc.CONTROLLER_DB_NUM))

    def get_if_bw(self, if_uri):
        # Get interface up-link and down-link bandwidth by its uri
        # if_uri: {node_name}:{if_name}, string
        # return: (timestamp, input_bw, output_bw, unit), string
        data = json.loads(self.redis.lrange(if_uri + ':traffic statistics', 0,0)[0])
        traffic_stat = data['stats'][0]
        return data['timestamp'], traffic_stat['input-bps'][0]['data'], traffic_stat['output-bps'][0]['data'], 'bps'

    def get_link_bw(self, node1, node2):
        # Get link  bandwidth by (node1, node2) (string,string)
        # (string,string)->(node_ip,node_ip)->(link_if, link_if)->if
        # return: (timestamp, input_bw, output_bw, unit), string

        ip_1 = sc.node_ip_map[node1]
        ip_2 = sc.node_ip_map[node2]

        if int(ip_1.split('.')[-1]) > int(ip_2.split('.')[-1]):
            ip_1, ip_2 = ip_2, ip_1

        link = sc.node_link_map[(ip_1, ip_2)]

        start_if = link.split('_')[0].lstrip('L')

        node1 = sc.ip_node_map[sc.if_node_map[start_if]]
        start_if_uri = node1 + ':' + sc.if_ip_name_map[start_if]

        return float(self.get_if_bw(start_if_uri)[2])

    def get_link_rtt(self, node_1, node_2):
        # Get the most recent round trip time between two nodes
        # node_1: name of the start node, string    
        # node_2: name of the end node, string
        # return: (timestamp, rtt, unit), float
        ip_1 = sc.node_ip_map[node_1]
        ip_2 = sc.node_ip_map[node_2]
        
        if int(ip_1.split('.')[-1]) > int(ip_2.split('.')[-1]):
            node_1, node_2 = node_2, node_1
        try:
            data = json.loads(self.redis.lrange(node_1+':'+node_2+':latency', 0, 0)[0])
        except:
            data = json.loads(self.redis.lrange(node_2+':'+node_1+':latency', 0, 0)[0])
        return data['rtt-average(ms)']

    def get_path_rtt(self, node_list):
        # Get the rtt along the given path (indicated by the list of nodes) 
        # node_list: list of names of nodes, [string]
        # return: (timestamp, rtt, unit), float
        timestamp = self.get_link_rtt(node_list[0], node_list[1])[0]
        rtt = 0.0
        for i in range (0, len(node_list) - 1):
            rtt += self.get_link_rtt(node_list[i], node_list[i+1])[1]
        return timestamp, rtt, 'ms'

    def get_links_rtt(self, link_list):
        # Get rtt of links in the link_list by pipeline
        # link_list: list of names of end nodes of a link, [(string, string)]
        # return: dict of rtt, dict[string] = float
        pipeline = self.redis.pipeline()
        rtt_list = {}
        for link in link_list:
            ip_1 = sc.node_ip_map[link[0]]
            ip_2 = sc.node_ip_map[link[1]]
            if int(ip_1.split('.')[-1]) < int(ip_2.split('.')[-1]):
                node_1, node_2 = link[0], link[1]
            else:
                node_1, node_2 = link[1], link[0]
            #print (node_1, " and", node_2)
			
            # Has to hard code this since there's no data for the link houston->tampa (another inconsitency!)
            if node_1 == 'houston' and node_2 == 'tampa':
                node_1, node_2 = 'tampa', 'houston'
            pipeline.lrange(node_1+':'+node_2+':latency', 0, 0)[0]
        #with open("debug.txt","w") as f:
        #    f.write(json.dumps(pipeline.execute(), indent = 4))
        bare_data = pipeline.execute()
        #print json.loads(bare_data[0][0])["rtt-average(ms)"]
        #print "hey!", self.redis.lrange('chicago:san francisco:latency', 0, -1)
        for item in bare_data:
            if (not item is None) and (not item == []):
                endA = json.loads(item[0])["from-router"]
                endZ = json.loads(item[0])["to-router"]
                rtt_list[(endA, endZ)] = json.loads(item[0])["rtt-average(ms)"]
        return rtt_list		

    def init_influx_client(self):
        host = sc.VM_EAST
        port = sc.INFLUX_PORT   
        user = sc.INFLUX_USER
        password = sc.INFLUX_PASSWORD
        dbname = sc.INFLUX_NAME
        self.influx = InfluxDBClient(host, port, user, password, dbname)

        try:
            self.influx.create_database(dbname)
            print("--> Create database: " + dbname)
        except:
            print("==> Database " + dbname + " already exist.")

    def write_to_influx(self, data_frame):
        # print("Write points: {0}".format(json_body))
        # client.write_points(json_body)
        pass


if __name__ == "__main__":
    cd = Controller_db.from_new_redis()
    #print '--> Link rtt : ', cd.get_link_rtt('tampa', 'houston')
    while True:
        print cd.get_link_bw('tampa','new york')
    # cd.init_influx_client()
    # while True:
    #     print '--> Path rtt : ', cd.get_path_rtt(['new york', 'miami', 'dallas', 'san francisco'])
    #     print '--> Link rtt : ', cd.get_link_rtt('tampa', 'houston')
    #     print '--> Bandwidth: ', cd.get_if_bw('new york:ge-1/0/3')


