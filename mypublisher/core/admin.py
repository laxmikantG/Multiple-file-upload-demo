'''
Created on 13-Feb-2014

@author: laxmikant
'''
from django.contrib import admin
from mypublisher.core.models import Files, FileAttributes

admin.site.register(Files)
admin.site.register(FileAttributes)