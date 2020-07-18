#!/bin/python3

import socket
import sys

try:
    HOST = '10.0.0.2'  # The server's hostname or IP address
    PORT = 1337    # The port used by the server

    try:
        flag = sys.argv[1]
    except IndexError:
        print('\n'+"Made by @elbee_ez")
        print('\n'+"Usuage: python3 sendFlag.py <FLAG>")
        print('\n')
        sys.exit()

 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(flag.encode('utf-8'))
            data = s.recv(1024).decode()
    
    print("Flag sent to flagbot")

    if('\n' in str(data)):
        data = str(data); data = data.replace('\n','')

    print('\n'+'Reply from flag bot: ', str(data))

except KeyboardInterrupt:
    print("Cancelling..")
    sys.exit()

