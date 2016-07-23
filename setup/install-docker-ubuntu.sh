#!/bin/bash

# Install Docker on Ubuntu versions according to the official documentation: 
# https://docs.docker.com/engine/installation/linux/ubuntulinux/
# Updated on: 2016-05-24	Author: Silvery Fu

if [ $# -eq 0 ]; then
	echo "--> No argument provided; please run as .sh UBUNTU_VERSION"
	echo "--> For example: .sh 14.04"
	exit
fi

UBUNTU_VER=$1
PRECISE_VER="12.04"; TRUSTY_VER="14.04"; WILY_VER="15.10"; XENIAL_VER="16.04"

# Update apt sources
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo touch /etc/apt/sources.list.d/docker.list
sudo chmod 666 /etc/apt/sources.list.d/docker.list

if [ "$UBUNTU_VER" == "$PRECISE_VER" ]; then
	# Install apparmor
	sudo apt-get install -y apparmor
	sudo echo "deb https://apt.dockerproject.org/repo ubuntu-precise main" > /etc/apt/sources.list.d/docker.list

elif [ "$UBUNTU_VER" == "$TRUSTY_VER" ]; then
	# Install apparmor
	sudo apt-get install -y apparmor
	# Install linux-image-extra
	sudo apt-get install -y linux-image-extra-$(uname -r)
	sudo echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list

elif [ "$UBUNTU_VER" == "$WILY_VER" ]; then
	# Install linux-image-extra
	sudo apt-get install -y linux-image-extra-$(uname -r)
	sudo echo "deb https://apt.dockerproject.org/repo ubuntu-wily main" > /etc/apt/sources.list.d/docker.list

elif [ "$UBUNTU_VER" == "$XENIAL_VER" ]; then
	# Install linux-image-extra
	sudo apt-get install -y linux-image-extra-$(uname -r)
	sudo echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" > /etc/apt/sources.list.d/docker.list

else
	echo "--> Error: No matched version"
	exit
fi

# Install Docker
sudo apt-get update
sudo apt-get install -y docker-engine
sudo service docker start

sudo docker run hello-world


