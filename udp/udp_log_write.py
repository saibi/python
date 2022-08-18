#!/usr/bin/env python3
# coding=utf8

import sys
import argparse
import socket 
import datetime
import os
import shutil

BUFSIZE = 512

def log_receiver(port, dir, sz):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('', port))

	while 1:
		data, addr = s.recvfrom(BUFSIZE)
		timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
		msg = timestamp + ' ' + data.decode('utf-8', errors='ignore').strip()
		msg = msg.replace('\n', '\n' + timestamp + ' ') + '\n'

		filename = 'log_' + addr[0] + ".txt"
		if dir != None and os.path.isdir(dir):
			log_path = os.path.join(dir, filename)
		else: 
			log_path = filename

		with open(log_path, "a" ) as f:
			f.write(msg)
		
		file_size = os.path.getsize(log_path)
		if file_size > sz:
			shutil.move(log_path, log_path + '.bak')


if __name__ == '__main__': 
	parser = argparse.ArgumentParser(description='udp log receiver') 
	parser.add_argument('-p', '--port', action="store", dest="port", type=int, help='listen port (8270)' ) 
	parser.add_argument('-d', '--dir', action="store", dest="dir", type=str, help='save direcotry') 
	parser.add_argument('-s', '--size', action="store", dest="size", type=int, help='log file size(mb)') 

	given_args = parser.parse_args()  
	port = given_args.port
	if port == None:
		port = 8270
	dir = given_args.dir
	mb = given_args.size
	if mb == None:
		mb = 1

	print('start udp log server. port:{0}, dir:{1}, size:{2}mb'.format(port, dir, mb))
	log_receiver(port, dir, mb * 1024*1024) 
