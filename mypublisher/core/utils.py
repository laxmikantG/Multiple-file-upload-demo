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
import json
from django.conf import settings

class ConfigParser(ConfigParser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d
    
    def write_ini_file (self, output_file_name,  cfgfilejson = {}):
        """
        """
        print cfgfilejson
        cfgfile = open(output_file_name, 'w')
        for section, ini_data in cfgfilejson.items():
            self.add_section(section)
            for key, value in ini_data.iteritems():
                self.set(section, key, value)
        self.write(cfgfile)
        cfgfile.close()
                
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
        config = ConfigParser()
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
#         print ret_dict,  str(error_code)
        return ret_dict.get(str(error_code), 500)
    
    def write_ini_file(self, output_file_name, json_dict):
        config = ConfigParser()
        config.write_ini_file(output_file_name, json_dict)

    def update_mime_types_to_ini(self):
        """
        """
        output_file_name = "/home/laxmikant/workspace/mypublisher/mypublisher/media/ini/mime_types.ini"
        cfgfile_json = open("/home/laxmikant/workspace/mypublisher/mypublisher/media/json/mimetypes.json").read()
        json_dict = {}
        cfgfilejson = json.loads(cfgfile_json)
        cfgfilejson = [json_dict.update(i) for i in cfgfilejson]
        ini_data = self.process_json_dict(json_dict)
        self.write_ini_file(output_file_name, ini_data)
        
    def process_json_dict(self, cfgfilejson):
        """
        """
        text_mimes = {}
        audio_mimes = {}
        video_mimes = {}
        image_mimes = {}
        zip_mimes = {}
        xml_mimes = {}
        
        for key, value in cfgfilejson.items():
            [val1, val2] = value.split("/")
            if self.match_text(val1, val2, "text") or self.text_contains(val1, val2, "text") :
                text_mimes.update({key :value})
            if self.match_text(val1, val2, "audio") or  self.text_contains(val1, val2, "audio") :
                audio_mimes.update({key :value})
            if self.match_text(val1, val2, "video")  or  self.text_contains(val1, val2, "video") :
                video_mimes.update({key :value})
            if self.match_text(val1, val2, "image")  or  self.text_contains(val1, val2, "image") :
                image_mimes.update({key :value})
            if  self.text_contains(val1, val2, "zip") or self.text_contains(val1, val2, "octet-stream") or  self.text_contains(val1, val2, "archive"):
                zip_mimes.update({key :value})
            if  self.text_contains(val1, val2, "xml"):
                xml_mimes.update({key :value})
#             else:
#                 pass
# #                 print value
        return {
          "text":text_mimes,
          "audio" : audio_mimes,
          "video": video_mimes,
          "zip": zip_mimes,
          "xml": xml_mimes
         }           

    def match_text(self, text1, text2, text):
        return text1 == text or text2 == text
    
    def text_contains(self, text1, text2, text):
        return text1.__contains__(text) or text2.__contains__(text)
    
if __name__ == '__main__':
    u = Utility()
    u.update_mime_types_to_ini()
#     print(u.guid("text"))
    