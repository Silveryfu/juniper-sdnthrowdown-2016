#vist the newest interface traffic updates in redis
#latest time of each interface traffic update differs




import sys_constant as sc
import redis
import json



r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
#scan all interface
for router in sc.routers:
    for interface_current in router['interfaces']:
        #interface name:traffic statistics
        interface_traffic_index = router['name'] + ':'+ interface_current['name']+':traffic statistics'
        d= json.loads(r.lrange(interface_traffic_index, 0,-1)[0]) #in time 0
        
        #print input-bps of all link interface in the newest update in redis
        #possible peek choice: 'output-bps'
        
        print interface_traffic_index
        print d['stats'][0]['input-bps'][0]['data']
        print '\n'


###write out all input bps in timespan
##for time_step in r.lrange('chicago:ge-1/0/2:traffic statistics', 0,-1):
##    d = json.loads(time_step)
##    print d['stats'][0]['input-bps'][0]['data'] #input-bps data
    

