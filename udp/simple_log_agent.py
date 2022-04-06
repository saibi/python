#!/usr/bin/env python3
# coding=utf8

import sys
import argparse
import socket 

BUFSIZE = 512
UPACKET_HEADER = "u42b 1 0 10\n"

def log_agent(addr, port):

    dest_addr = (addr, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 0))
    my_port = s.getsockname()[1]

    print('start simple udp log agent :', my_port)

    upacket = UPACKET_HEADER + "ct log udpa"
    s.sendto(upacket.encode('utf-8'), dest_addr)

    while 1:
        data, addr = s.recvfrom(BUFSIZE)
        print(data.decode('utf-8').strip(),)


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='simple udp log agent') 
    parser.add_argument('-a', action="store", dest="addr", type=str, required=True, help="DMC b/d IP address")
    parser.add_argument('-p', action="store", dest="port", type=int, required=True, help="DMC b/d port") 
    given_args = parser.parse_args()  
    addr = given_args.addr
    port = given_args.port 

    log_agent(addr, port) 
