'''
Created on 13-Feb-2014

@author: laxmikant
'''
import time
import random
import socket
import hashlib

class Utility:
    
    def __init__(self):
        """
        """
        pass
    
    def guid(self, *args ):
        """
        Generates a universally unique ID.
        Any arguments only create more randomness.
        """
        t = long( time.time() * 1000 )
        r = long( random.random()*100000000000000000L )
        try:
            a = socket.gethostbyname( socket.gethostname() )
        except:
            # if we can't get a network address, just imagine one
            a = random.random()*100000000000000000L
        data = str(t)+' '+str(r)+' '+str(a)+' '+str(args)
        data = hashlib.md5(data).hexdigest()
    
        return data

if __name__ == '__main__':
    pass