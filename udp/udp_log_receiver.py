#!/usr/bin/env python3
# coding=utf8

import sys
import argparse
import socket 

BUFSIZE = 512

def log_receiver(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', port))

    print('udp log server ready')

    while 1:
        data, addr = s.recvfrom(BUFSIZE)
        print(data,)


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='udp log receiver') 
    parser.add_argument('-p', '--port', action="store", dest="port", type=int, required=True) 
    given_args = parser.parse_args()  
    port = given_args.port 

    log_receiver(port) 
