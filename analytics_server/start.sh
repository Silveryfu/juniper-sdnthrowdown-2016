#!/bin/bash

echo "--> Starting monitor agent..."
./start-influx-conta.sh
./start-cadvisor-conta-connect-influx.sh
./start-grafana-conta-connect-influx.sh

echo "--> Monitor agent started."
