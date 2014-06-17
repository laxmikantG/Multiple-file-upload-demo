'''
Created on 13-Feb-2014

@author: laxmikant
'''
from django.contrib import admin
from mypublisher.core.models import Files,FileAttributes, FileSizeUnit\
    , FilePermissions, FileMetaData, UserFiles 

admin.site.register(Files)
admin.site.register(UserFiles)
admin.site.register(FileAttributes)
admin.site.register(FileSizeUnit)
admin.site.register(FilePermissions)
admin.site.register(FileMetaData)