'''
Created on 13-Feb-2014

@author: laxmikant
'''
import time
import random
import socket
import hashlib
from mimetypes import MimeTypes
import urllib 


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
    
    def guess_mime_type(self, file_name):
        '''
        '''
        mime = MimeTypes()
        url = urllib.pathname2url(file_name)
        mime_type = mime.guess_type(url)
        return  mime_type

if __name__ == '__main__':
    pass