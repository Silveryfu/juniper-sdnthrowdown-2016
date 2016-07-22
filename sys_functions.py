'''
Created on July 21, 2016

@author: Stephen Zhu, Yuchi Chen, and Silvery Fu
'''
import requests
requests.packages.urllib3.disable_warnings()
import json
import pprint
import sys_constant as sc

# Get interface_id by router name
# start: start router name
# endL:  end router name

def get_if_by_router(start, end):
