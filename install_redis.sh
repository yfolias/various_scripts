#!/bin/bash

# Yannis Folias - 13/02/2019
# Redis installation script on Centos Server 6.10

function download(){
	echo "[+] Downloading Redis Server..."
	wget http://download.redis.io/redis-stable.tar.gz
	tar xvzf redis-stable.tar.gz
	cd redis-stable
	make
	cp src/redis-server /usr/local/bin/
	cp src/redis-cli /usr/local/bin/
}

function createDirs(){
	echo "[+] Creating necesary directories..."
	mkdir /etc/redis
	mkdir /var/redis
	mkdir /var/redis/6379
	echo "[+] Copying configuration files..."
	cp utils/redis_init_script /etc/init.d/redis_6379
	cp ../6379.conf /etc/redis/6379.conf
	chkconfig --add redis_6379
}

function main(){
	echo "[+] Redis Server Installation begins $(date -u)"
	sleep 1
	download
	createDirs
	echo "[+] Starting Redis Server..."
	service redis_6379 start
	sleep 1
	echo "[+] Please test Redis functionality 'redis-cli ping' "	
}

main
