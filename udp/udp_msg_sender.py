#!/usr/bin/env python3
# Python Network Programming Cookbook, Second Edition -- Chapter - 1 
# This program is optimized for Python 2.7.12 and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket 
import sys 
import argparse 
 
data_payload = 2048 
 
def echo_client(addr, port, broadcast, message): 
    """ A simple echo client """ 
    # Create a UDP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    if broadcast == True:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1 ) # broadcast
 
    server_address = (addr, port) 
    print ("Connecting to %s port %s" % server_address) 
 
    try: 
 
        # Send data 
        print ("Sending [%s]" % message) 
        upacket = "42b 10\n" + message
        sent = sock.sendto(upacket.encode('utf-8'), server_address) 
 
        # Receive response 
        data, server = sock.recvfrom(data_payload) 
        print ("received [%s]" % data) 
 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 
 
if __name__ == '__main__': 
    parser = argparse.ArgumentParser             (description='Socket Server Example') 
    parser.add_argument('-p', '--port', action="store", dest="port", type=int, required=True) 
    parser.add_argument('-a', '--addr', action="store", dest="addr", type=str, default='localhost', required=False)
    parser.add_argument('-b', '--broadcast', action='store_true', dest='broadcast')
    parser.add_argument('message', nargs=argparse.REMAINDER) 
    given_args = parser.parse_args()  
    port = given_args.port 
    addr = given_args.addr
    broadcast = given_args.broadcast
    message = ' '.join(given_args.message)

    echo_client(addr, port, broadcast, message) 
