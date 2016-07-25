#!/bin/bash

# Updated on: 2016-05-25	Author: Silvery Fu

echo "--> Configuring container tools..."
sudo nohup ./install-docker-ubuntu.sh $(lsb_release -r | awk '{print $2}') >/dev/null 2>&1 &

wait $!
echo "--> Configuration completed."

echo "--> Configuring cadvisor and influx..."
sudo nohup ./install-cadvisor-conta.sh >/dev/null 2>&1 &
sudo nohup ./install-influx-conta.sh >/dev/null 2>&1 &
sudo nohup ./install-grafana-conta.sh >/dev/null 2>&1 &

wait $!
echo "--> Configuration completed."

