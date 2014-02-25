'''
Created on 08-Feb-2014

@author: laxmikant
'''
import os
import settings
from mypublisher.core.utils import Utility as UTILITY
from mypublisher.core.file_manager import FileManager as FILES_MANAGER
from mypublisher.core.error_handler import ErrorHandler as ERROR_HANDLER

class ContentManager():
    '''
    Content related operations
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    def handle_uploaded_file(self, files, req_dict):
        ''' 
        '''
        for f in files:
            if not os.path.exists(settings.CONTENT_STORAGE_PATH):
                try:
                    os.makedirs(settings.CONTENT_STORAGE_PATH, 0644)
                except OSError, e:
                    writelog("Folder can not be created \n"+str(e))
            content_storage_path = os.path.join(settings.\
                                              CONTENT_STORAGE_PATH, f.name)
            try:
                with open(content_storage_path, 'wb+') as destination:
                    os.chmod(content_storage_path, 0600)
                    for chunk in f.chunks():
                        destination.write(chunk)
                file_meta = {"file_path":content_storage_path, "file_name"\
                        :f.name, "description":req_dict.get("description")}
                message = self.create_file_meta_dict(file_meta)
            except OSError, e:
                    writelog("File can not be created \n"+str(e))
                    return False
        return True
            
    def create_file_meta_dict(self, file_meta):
        data_dict = {}
        path = file_meta["file_path"]
        data_dict["size"] = os.path.getsize(path)
        utils = UTILITY() 
        data_dict["mimetype"] = utils.guess_mime_type(file_meta["file_name"])
        data_dict["description"] = file_meta["description"]
        data_dict["extension"] = utils.get_extension(file_meta["file_name"])
        data_dict["location"] = file_meta["file_path"]
        data_dict["name"] = file_meta["file_name"]
        
        files_manager = FILES_MANAGER()
        files_manager.create_Files_record(data_dict)
        return True
                
                
def writelog(data):
    '''
        Write log file
    '''
    fp = open("/tmp/error_log.log", "w")
    fp.write(str(data))
    fp.close()