'''
Created on 13-Feb-2014

@author: laxmikant
'''
import os
import time
import random
import socket
import hashlib
import ConfigParser
from mimetypes import MimeTypes
import urllib 
from django.conf import settings

class ConfigParser(ConfigParser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d        

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
        return  mime_type[0]
    
    def get_request_dict(self, request, method="POST"):
        ''' 
        '''
        if method == "GET":
            req_dict = dict(zip(request.GET.keys(),request.GET.values()))
        else:
            req_dict = dict(zip(request.POST.keys(),request.POST.values()))
        return req_dict

    def read_config_file(self, filename):
        '''
        '''
        config = ConfigParser.ConfigParser()
        config.read(filename)
        return config
    
    def get_extension(self, filename):
        (name, extension) = os.path.splitext(filename)
        return extension
    
    def load_config(self, filepath):
        """
        returns a dictionary with keys of the ini
        """
        f = ConfigParser()
        f.read(filepath)
        d = f.as_dict()
        all_vals = {}
        {all_vals.update(dct) for title, dct in d.iteritems()}
        return all_vals

    def get_err_msg(self, error_code):
        """
        """
        fp = settings.ERROR_CODES_INI
        ret_dict = self.load_config(fp)
        print ret_dict,  str(error_code)
        return ret_dict.get(str(error_code), 500)


if __name__ == '__main__':
    u = Utility()
    print u.get_err_msg(404)
#     print(u.guid("text"))
    