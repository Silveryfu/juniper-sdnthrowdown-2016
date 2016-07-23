'''
Created on July 22, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''

import redis
import json
import sys
import threading
import sys_constant as sc


class Link_event_handler(threading.Thread):
    def __init__(self, r):
        threading.Thread.__init__(self)

        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe('link_event')

    @classmethod
    def from_new_redis(cls):
        return cls(redis.StrictRedis(host=sc.CONTROLLER_DB_URI,
                                         port=sc.CONTROLLER_DB_PORT,
                                         db=sc.CONTROLLER_DB_NUM))

    def run(self):
        for item in self.pubsub.listen():
            print item['channel'], ":", item['data']
            if isinstance(item['data'], basestring):
                event = json.loads(item['data'])
                self.handle(event)

    def handle(self, event):

        pass

if __name__ == "__main__":
    handler = Link_event_handler.from_new_redis()
    handler.start()