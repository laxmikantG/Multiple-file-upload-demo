'''
Created on 08-Feb-2014

@author: laxmikant
'''
import os
import settings

from mypublisher.core import file_manager as FILES_MANAGER

class ContentManager():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def handle_uploaded_file(self, files):
        ''' '''
        for f in files:
            content_storage_path = os.path.join(settings.CONTENT_STORAGE_PATH, f.name)
            try:
                with open(content_storage_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                files = FILES_MANAGER()
                {"file_path":content_storage_path, "file_name":f.name, }
            except Exception, e :
                raise e
                
                
def writelog(data):
    '''
        Write log file
    '''
    fp = open("/tmp/error_log.log", "w")
    fp.write(str(data))
    fp.close()