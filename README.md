SYS-V
==

SYS-V is an SD-WAN optimizer on [Juniper NorthStar SDN controller](http://www.juniper.net/us/en/products-services/sdn/northstar-network-controller/). It contains three major components:

1. Topology Discovery
  * sys_ep_request.py: methods to launch API requests with the controller.
  * sys_db_request.py: methods to retrieve data from controller database server.

2. Path Computation
  * sys_path_compute.py: methods to compute path.

3. State Installation
  * sys_path_update.py: methods to install path; It also contains high-level methods for Topology Discovery

+ Other modules:
  * sys_constant.py: credentials, constants and mappings.
  * sys_main.py: management loop.
