#!/bin/env python
# -*- coding: utf-8 -*-

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9911))

print s.recv(1024)

for data in ['zhang','liu','wang']:
	s.send(data)
    	print s.recv(1024)

s.send('exit')
s.close()
