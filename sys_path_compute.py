import sys_constant as sc
import heapq
import sys
from collections import defaultdict
from sys_db_request import Controller_db
from sys_path_update import Lsp_update
from sys_ep_request import Ep_request
from pprint import pprint


class Path_compute:
    def __init__(self, cd=Controller_db.from_new_redis(), lu=Lsp_update(), er=Ep_request()):
        self.cd = cd
        self.lu = lu
        self.er = er

    def get__adjacent_list(self, forged = None, status = None):
        self.adj_dict, self.edge_dict = self._adjacent_list(forged_link = forged, status = status)

    def compute(self, start='san francisco', end='new york'):
        return self.dijkstra(self.adj_dict, self.edge_dict, start, end)


    def compute_node_disjoint_path(self, node1, node2):
        adj_dict,edge_dict = self._adjacent_list()

        path_one = self.dijkstra(adj_dict, edge_dict, node1,node2)

        for node in path_one[1:-1]:
            del adj_dict[node]

        for  key in adj_dict:
            for node in path_one[1:-1]:
                if node in adj_dict[key]:
                    adj_dict[key].remove(node)

        if len(adj_dict['new york']) !=0 and len(adj_dict['san francisco']) !=0 :
            path_two = self.dijkstra(adj_dict, edge_dict, node1,node2)
        else:
            print 'used up all node, no node disjoint path'

        return path_one, path_two


    def compute_link_disjoint_path(self,node1,node2):
        adj_dict,edge_dict = self._adjacent_list()

        path_one = self.dijkstra(adj_dict, edge_dict, node1,node2)
        #print path_one

        for index in range(len(path_one)):
            if index < len(path_one)-1:
                edge_dict[(path_one[index],path_one[index+1])] = sys.maxint

        path_two = self.dijkstra(adj_dict, edge_dict, node1,node2)
        #print path_two
        
        return path_one, path_two

    def compute_constrained_shortest_path(self, constraint_type='bw', constraint=0.0, node1='san francisco',node2='new york'):
        edge_dict = {}
        adj_dict = defaultdict(list)
        for link in self.lu.get_all_link():
            value = -1
            if constraint_type == 'bw':
                value = 1000000000 - 1000 * self.cd.get_link_bw(link[0], link[1])
            elif constraint_type == 'rtt':
                value = self.cd.get_link_rtt(link[0], link[1])
            else:
                value = 1000000000 - 1000 * self.cd.get_link_bw(link[0], link[1])
            if value > constraint:
                edge_dict[link] = self.cd.get_link_bw(link[0], link[1])
            else:
                edge_dict[link] = sys.maxint 
            adj_dict[link[0]].append(link[1])
            adj_dict[link[1]].append(link[0])

        path = self.dijkstra(adj_dict, edge_dict, node1,node2)

        for index in range(len(path)):
            ip_1 = sc.node_ip_map[path[index]]
            ip_2 = sc.node_ip_map[path[index+1]]

            if int(ip_1.split('.')[-1]) > int(ip_2.split('.')[-1]):
                path[index], path[index+1] = path[index + 1], path[index]

            if edge_dict[(path[index],path[index+1])] >= sys.maxint:
                return []
            else:
                return path
                
    def dijkstra(self, adj, edge_dict, start='san francisco', end='new york'):
        # Compute and generate an updated ERO marked by node names
        # return: path, list
        node_list = []

        for node in self.er.ep_get_node():
            try:
                node_list.append(sc.ip_node_map[node['name'].encode('ascii')])
            except:
                continue
        adj_dict=adj
        edge_dict = edge_dict

        q = [(0, start, ())] # Heap of (cost, path_head, path_rest)
        visited = set()      # visited nodes

        while True:
            (cost, n1, path) = heapq.heappop(q)
            if n1 not in visited:
                visited.add(n1)
                if n1 == end:
                    path = (path, n1)
                    path_list = []
                    while len(path) > 0:
                        path_list.insert(0, path[1])
                        path = path[0]
                    return path_list
                path = (path, n1)
                for neighbor in adj_dict[n1]:
                    if neighbor not in visited:
                        try:
                            if (n1, neighbor) in edge_dict:
                                cost_add = edge_dict[(n1, neighbor)]
                            else:
                                cost_add = edge_dict[(neighbor, n1)]
                            heapq.heappush(q, (cost + cost_add, neighbor, path))
                        except:
                            continue

    def _adjacent_list(self, forged_link = None, status = None):
        ''''
        edge_dict = {}
        adj_dict = defaultdict(list)
        for link in self.lu.get_all_link():
            if link == forged_link and status == "down":
                continue
            if self._check_link_status(link):
                edge_dict[link] = self.cd.get_link_rtt(link[0], link[1]) #***slow
                adj_dict[link[0]].append(link[1])
                adj_dict[link[1]].append(link[0])
        return adj_dict, edge_dict
        '''
        edge_dict = {}
        adj_dict = defaultdict(list)
        link_list = self.lu.get_all_link()
        if forged_link in link_list and status == "down":
            link_list.remove(forged_link)
        # generate adj_dict
        for link in link_list:
            adj_dict[link[0]].append(link[1])
            adj_dict[link[1]].append(link[0])

        # generate edge_dict
        rtt_list = self.cd.get_links_rtt(link_list)
        for link in rtt_list:
            edge_dict[link] = rtt_list[link]
        return adj_dict, edge_dict

    def _check_link_status(self, link):
            endA_IP = sc.node_ip_map[link[0]]
            endZ_IP = sc.node_ip_map[link[1]]
            return True
            # if self.lu.get_link_status((endA_IP, endZ_IP)) == "Up":  #***slow
            #     return True
            # else:
            #     return False

    def link_node_map(self):
        link_node_map = sc.link_node_map
        node_link_dict = dict()
        for link in link_node_map:
            node_link_dict[link_node_map[link]] = link

        print node_link_dict
            
        #print sc.if_link_map

if __name__ == "__main__":
    pc = Path_compute()
    #adj_dict,edge_dict = pc.adjacent_list()
    #print pc.compute_node_disjoint_path('san francisco','new york')
    #print pc.compute(adj_dict, edge_dict, 'san francisco','new york')
    #print pc.compute_link_disjoint_path('san francisco','new york')
    #print pc.compute('san francisco','new york')
    #print pc.compute_constrained_shortest_path(constraint=2, node1='san francisco',node2='new york')
    #print pc.compute_constrained_shortest_path(constraint=5, node1='san francisco',node2='new york')
    # pc.link_node_map()
    adj, edge = pc._adjacent_list(forged_link = ('san francisco', 'chicago'), status = "down")
    pprint(edge)





