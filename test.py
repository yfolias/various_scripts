#!/usr/bin/python
# Sample script for running parallel system commands
# Yannis Folias

import threading 
import time
import os

def myFunc(n, cmd):
	os.system(cmd + ' >> logs/' + cmd  +'.log')
	time.sleep(n)
	
n = int(input("Amount of secs: "))
cmds = ['uptime', 'id', 'ifconfig']

for cmd in cmds:
	t = threading.Thread(target = myFunc, args = (n, cmd))
	t.start()
