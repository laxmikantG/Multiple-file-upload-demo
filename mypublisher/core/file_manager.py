'''
Created on 13-Feb-2014

@author: laxmikant
'''

import models
 
class FileManager:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''

    def create_Files_record(self, file_meta):
        m = models.Files(**file_meta)
        m.save()
    
    def updateFileAttributes(self, file_meta):
        m = models.FileAttributes(**file_meta)
        m.save()
        
    def updateFilePermissions(self, file_meta):
        m = models.FilePermissions(**file_meta)
        m.save()

    def getfilesbyuser(self, user):
        return models.UserFiles.objects.filter(user__username = user)
    
        


def writelog(data):
    ''' Write log file'''
    fp = open("/tmp/error_log.log", "a")
    fp.write(str(data))
    fp.close()