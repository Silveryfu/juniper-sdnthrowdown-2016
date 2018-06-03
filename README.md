SYS-V
==

SYS-V is an SD-WAN optimizer on [Juniper NorthStar SDN controller](http://www.juniper.net/us/en/products-services/sdn/northstar-network-controller/). It consists of three major components:

1. Topology Discovery
  * sys_ep_request.py: methods to launch API requests with the controller.
  * sys_db_request.py: methods to retrieve data from controller database/redis server.

2. Path Computation
  * sys_path_compute.py: methods to compute path.

3. State Installation
  * sys_path_update.py: methods to install path; It also contains high-level methods for Topology Discovery

+ Other modules:
  * sys_constant.py: credentials, constants and mappings.
  * sys_main.py: management loop.

System Overview
==

Interactive video streaming refers to the class of rapidly emerging video applications that involve both streaming video content to viewers and rich interactions between the viewers and video producers.

![arch](https://i.imgur.com/AKNX002.jpg)

Examples include [Cloud Gaming](https://en.wikipedia.org/wiki/Cloud_gaming), Streaming AR, and VDI; more information can be found in our papers:

- [*"Rhizome: Utilizing the Public Cloud to Provide 3D Gaming Infrastructure"*, ACM MMSys'15](https://dl.acm.org/citation.cfm?id=2713190)
- [*"Cloud Gaming: Understanding the Support From Advanced Virtualization and Hardware"*, IEEE TCSVT'16](https://dl.acm.org/citation.cfm?id=3084012)
- [*"Bridging Online Game Playing and Live Broadcasting: Design and Optimization"*, ACM NOSSDAV'15](https://dl.acm.org/citation.cfm?id=2736089)
- [*"Towards Fully Offloaded Cloud-based AR: Design, Implementation and Experience"*, ACM MMSys'17](https://dl.acm.org/citation.cfm?id=3084012)

In a nutshell, the SYS-V controller leverages application/video streaming-level information to manage traffic, providing network-level supports for interactive video streaming.
![arch](https://i.imgur.com/xVw6o9w.jpg?1)

A brief demo can be found [here](https://www.youtube.com/watch?v=oBlFaZwybxc). Full presentation with the demo of live interacitve video streaming can be found [here](https://www.youtube.com/watch?v=R5Lqi7P6URU).

This project is the first place winner of *2016 Juniper-Telus SDN Throwdown Competition*. 

&copy;Stephen Chu, Yuchi Chen, and Silvery Fu


