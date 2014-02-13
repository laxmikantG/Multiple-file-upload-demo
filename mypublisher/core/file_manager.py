'''
Created on 13-Feb-2014

@author: laxmikant
'''
import os
from mypublisher.core.utils import Utility as UTILITY
import models
 
class FileManager(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''

    def store_files_in_db(self, file_meta):
        data_dict ={}
        data_dict.size = os.path.getsize(file_meta.file_path)
        
        utils = UTILITY() 
        data_dict.mimetype = utils.guess_mime_type(file_meta.file_name)
         
        data_dict.description = file_meta.description
        data_dict.extension = os.path.splitext(file_meta.file_name)[1]
        data_dict.location = os.path.join(file_meta.file_path, file_meta.file_name)
        data_dict.name =file_meta.file_name
        m = models.Files(**data_dict)
        m.save()