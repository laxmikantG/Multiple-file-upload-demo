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
                    return False, 10004  
        return True, 20001
            
    def create_file_meta_dict(self, file_meta):
        utils = UTILITY()
        data_dict = {}
        path = file_meta["file_path"]
        filename = file_meta["file_name"]
        extension = utils.get_extension(file_meta["file_name"])
        data_dict["size"] = os.path.getsize(path)
        mimetype = utils.guess_mime_type(file_meta["file_name"])
        data_dict["description"] = file_meta["description"]
        data_dict["extension"] = extension 
        data_dict["location"] = file_meta["file_path"]
        data_dict["name"] = filename 
        data_dict["mimetype"] = mimetype
        files_manager = FILES_MANAGER()
        files_manager.create_Files_record(data_dict)
        rets = self.get_file_attributes(extension, mimetype)
        
        file_meta = {
            "is_text": rets[0], 
            "is_archive": rets[1], 
            "is_hidden" :  rets[2],
            "is_image":  rets[3],
            "is_system_file": rets[4],
            "is_xhtml": rets[5], 
            "is_audio": rets[6], 
            "is_video": rets[7],
            "is_unrecognised": rets[8]
        }
        files_manager.updateFileAttributes(file_meta)
        return True

    def get_file_attributes(self, extension, mimetype):
        filetype = self.check_by_mime_type(mimetype)
        if not filetype:
            file_attribs = [
                self.is_text_file(extension, mimetype),
                self.is_archive_file(extension, mimetype),
                self.is_hidden_file(extension, mimetype),
                self.is_image_file(extension, mimetype),
                self.is_system_file(extension, mimetype),
                self.is_xhtml_file(extension, mimetype),
                self.is_audio_file(extension, mimetype),
                self.is_video_file(extension, mimetype)
            ]
            file_attribs.append(self.is_unrecognised_file(file_attribs))
            return file_attribs  
        else:
            return self.resolve_file_type_meta(filetype)
             
    def resolve_file_type_meta(self, filetype):
            conditions = [  # make a list: an iterable
               True and filetype == "text" or False, 
               True and filetype == "zip" or False, 
               True and filetype == "hidden" or False, 
               True and filetype == "image" or False,
               True and filetype == "system" or False, 
               True and filetype == "xml" or False, 
               True and filetype == "audio" or False, 
               True and filetype == "video" or False,
             ]
            conditions.append(self.is_unrecognised_file(conditions))
            return conditions 
            
    def  is_text_file(self, extension, mimetype):
        filetype = self.check_by_extension(extension)
        return filetype == "text"
    
    def is_archive_file(self, extension, mimetype):
        filetype = self.check_by_extension(extension)
        return filetype == "zip"
    
    def is_hidden_file(self, extension, mimetype):
        filetype = self.check_by_extension(extension)
        return filetype == "hidden"
    
    def is_system_file(self, extension, mimetype):
        filetype = self.check_by_extension(extension)
        return filetype == "system"
    
    def is_xhtml_file(self, extension, mimetype):
        filetype = self.check_by_extension(extension)
        return filetype == "xhtml"
    
    def is_audio_file(self, extension, mimetype):
        filetype = self.check_by_extension(extension)
        return filetype == "audio"
    
    def is_video_file(self, extension, mimetype):
        filetype = self.check_by_extension(extension)
        return filetype == "video"
    
    def is_image_file(self, extension, mimetype):
        filetype = self.check_by_extension(extension)
        return filetype == "image"

    def is_unrecognised_file(self, conditions):
        is_unrecognised = False
        # apply De Morgans
        if not any(conditions):
            is_unrecognised = True
        return is_unrecognised

    def check_by_mime_type(self, mimetype):
        filepath = settings.MIME_TYPES_INI
        utils = UTILITY()
        config_dict = utils.load_config_as_dict(filepath)
        return self.find_mime_type(config_dict, mimetype)
        
    def find_mime_type(self, nested_dict, value, prepath=()):
        section = None
        for item in nested_dict:
            result = {key:val for key, val in nested_dict[item].items() if value == val}
            if result:
                return item
        return section
    
    def check_by_extension(self, extension):
        filepath = settings.MIME_TYPES_INI
        utils = UTILITY()
        config_dict = utils.load_config_as_dict(filepath)
        for key, val in config_dict.items():
            if val.has_key(extension):
                return key 
        return None
#         config_data = utils.load_config(settings.MIME_TYPES_INI)
    
def writelog(data):
    ''' Write log file'''
    fp = open("/tmp/error_log.log", "a")
    fp.write(str(data))
    fp.close()