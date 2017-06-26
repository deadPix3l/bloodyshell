import socket
import threading
import string
import random

from extras import common

class Server(threading.Thread):
    clients = {}
    currentClient = None
    
    def __init__(self, port):
        super(Server, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('0.0.0.0', port))
        self.s.listen(5)
        
    def run(self):
        while True:
            conn, addr = self.s.accept()
            
            # create a unique name
            client_id = genName()
            while client_id in self.clients:
                client_id = genName()
                
            client = common.Client(conn, addr, uid=client_id)
            self.clients[client_id] = client
            
            
    def select_client(self, client_id):
        try:
            self.currentClient = self.clients[client_id] 
            
        except (KeyError, ValueError): 
            self.curentClient = None
        
        return self.currentClient

    def remove_client(self, key):
        return self.clients.pop(key, None)
        
        
    def listClients(self, action):
        print 'ID - Client Address'
        print '-------------------'
        for key in self.clients:
            print '{:>2} - {}'.format(key, self.clients[key].addr[0])
            
    def renameClient(self, action):
        if action in self.clients:
            print "name exists. nothing changed"
            return
        if not self.currentClient:
            print "please select a client first"
            return
        x = self.currentClient.uid
        del self.clients[x]
        self.clients[action] = self.currentClient
        self.currentClient.uid = action
        return self.currentClient
        

#####################################################

# supports 354,900 names
def genName(word=True):
    letters = string.ascii_lowercase
    vowels = 'aeoiu'
    other = [i for i in letters if i not in vowels]
    
    if not word:
        return ''.join(random.choice(letters) for i in range(5))
        
    a = [
        random.choice(letters),
        random.choice(vowels),
        random.choice(letters),
        random.choice(other),
        random.choice(vowels)
    ]
    return ''.join(a)
    



