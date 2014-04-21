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