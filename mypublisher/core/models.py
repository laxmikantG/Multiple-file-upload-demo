from django.db import models
import datetime
from django.contrib.auth.admin import User
from mypublisher.core.utils import Utility as UTILITY
# Create your models here.

def content_file_name(username, filename):
    return '/'.join(['content', username, filename])

class Files(models.Model):
    uid = models.TextField()
    name = models.TextField(blank=True, null=True)
    extension = models.CharField(blank=True, null=True, max_length=100)
    location = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    permissions =  models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    mimetype = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s ' % (self.name)
  
    def save(self):
        if self.pk is None:
            utils = UTILITY()
            self.uid = utils.guid()
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        super(Files, self).save()

        
class FileAttributes(models.Model):
    uid = models.TextField()
    is_text = models.SmallIntegerField(blank=True, null=True, help_text=
                                        "0|Is not a text. 1|Is not a text")
    is_archive = models.SmallIntegerField(blank=True, null=True, help_text=
                              "0|Is not an archive file. 1|Is an archive ")
    is_hidden = models.SmallIntegerField(blank=True, null=True, help_text=
                                      "0|Is not hidden file. 1|Is hidden ")
    is_image = models.SmallIntegerField(blank=True, null=True, help_text=
                                      "0|Is not hidden file. 1|Is hidden ")

    is_system_file = models.SmallIntegerField(blank=True, null=True, 
                   help_text="0|Is not a system file. 1|Is a system file ")
    is_xhtml = models.SmallIntegerField(blank=True, null=True, help_text=
                                    "0|Is not a xhtml file. 1|Is a xhtml ")
    is_audio = models.SmallIntegerField(blank=True, null=True, help_text=
                                  "0|Is not an audio file. 1|Is an audio ")
    is_video  = models.SmallIntegerField(blank=True, null=True, help_text=
                                    "0|Is not a video file. 1|Is a video ")
    is_unrecognised = models.SmallIntegerField(blank=True, null=True, 
         help_text="0|Format could not recognized, 1|Format is recognized")
    
    def __unicode__(self):
        return u'%s ' % (self.pk)

    def save(self):
        if self.pk is None:
            utils = UTILITY()
            self.uid = utils.guid()
        super(FileAttributes, self).save()
    

class FileSizeUnit(models.Model):
    unit_name = models.CharField(blank=True, null=True, max_length=10)
    unit_value = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s ' % (self.unit_name)
    
    
class FilePermissions(models.Model):
    uid = models.TextField()
    read = models.SmallIntegerField(blank=True, null=True)
    edit = models.SmallIntegerField(blank=True, null=True)
    full = models.SmallIntegerField(blank=True, null=True)
    none = models.SmallIntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s ' % (self.pk)
    
    def save(self):
        if self.pk is None:
            utils = UTILITY()
            self.uid = utils.guid()
        super(FilePermissions, self).save()
    
    
class FileData(models.Model):
    uid = models.TextField()
    blob = models.FileField(upload_to=content_file_name, blank=True, 
                                                                 null=True)
    text = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s ' % (self.pk)
    
    def save(self):
        if self.pk is None:
            utils = UTILITY()
            self.uid = utils.guid()
        super(FileData, self).save()


class FileMetaData(models.Model):
    uid = models.TextField()
    file = models.ForeignKey(Files, blank=True, null=True)
    attributes = models.ForeignKey(FileAttributes, blank=True, null=True)
    size = models.ForeignKey(FileSizeUnit, blank=True, null=True)
    permissions = models.ForeignKey(FilePermissions, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User)    

    def __unicode__(self):
        return u'%s ' % (self.file)
    
    def save(self):
        if self.pk is None:
            utils = UTILITY()
            self.uid = utils.guid()
            self.modified = datetime.datetime.today()
        super(FileMetaData, self).save()