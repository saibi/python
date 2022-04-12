#!/usr/bin/env python3
# Python Network Programming Cookbook, Second Edition -- Chapter - 1 
# This program is optimized for Python 2.7.12 and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket 
import sys 
import argparse 
 
data_payload = 2048 

UPACKET_HEADER = "u42b 1 0 1\n"
 
def echo_client(addr, port, broadcast, message, max): 
    """ A simple echo client """ 
    # Create a UDP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    if broadcast == True:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1 ) # broadcast
 
    server_address = (addr, port) 
    print ("Connecting to %s port %s" % server_address) 
 
    try: 
 
        # Send data 
        print ("Send {msg}. {n} times".format(msg=message, n=max)) 

        count = 0

        while count < max:
            print("sending #", count + 1)
            upacket = UPACKET_HEADER + message + " #" + str(count) 
            sent = sock.sendto(upacket.encode('utf-8'), server_address) 
            count += 1
 

    finally: 
        print ("Closing connection to the server") 
        sock.close() 
 
if __name__ == '__main__': 
    parser = argparse.ArgumentParser             (description='Socket Server Example') 
    parser.add_argument('-p', '--port', action="store", dest="port", type=int, required=True) 
    parser.add_argument('-a', '--addr', action="store", dest="addr", type=str, default='localhost', required=False)
    parser.add_argument('-b', '--broadcast', action='store_true', dest='broadcast')
    parser.add_argument('-n', action="store", dest="n", type=int, default=100, required=False)
    parser.add_argument('message', nargs=argparse.REMAINDER) 
    given_args = parser.parse_args()  
    port = given_args.port 
    addr = given_args.addr
    broadcast = given_args.broadcast
    n = given_args.n
    message = ' '.join(given_args.message)

    echo_client(addr, port, broadcast, message, n) 
