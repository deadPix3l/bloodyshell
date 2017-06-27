#!/usr/bin/env python
import string
import random
from extras import common
# Passive
# - Server side only commands

def help(_=''):
    print '''
        HELP MENU - <required> [optional]
    -------------------------------------------
    client <id>         - Connect to a client.
    clients             - List connected clients.
    download <file>     - Download a file.
    execute <command>   - Execute a command on the target.
    help                - Show this help menu.
    kill [client]        - Kill the client connection.
    persistence         - Apply persistence mechanism.
    quit                - Exit the server and end all client connections.
    rename <name>       - rename current client to "name"
    scan <ip>           - Scan top 25 TCP ports on a single host.
    selfdestruct        - Remove all traces of the RAT from the target system.
    survey              - Run a system survey.
    unzip <file>        - Unzip a file.
    upload <file>       - Upload a file.
    wget <url>          - Download a file from the web.
    '''
    
def quit(_):
    print "Goodbye!"
    exit(1)
