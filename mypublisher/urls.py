from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
#     (r'^statinfo/$', 'appname.views.stat_info'),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/login'}),
    (r'^menu/$', 'mypublisher.views.mainmenu'),
    
    (r'^cmanager/$', 'mypublisher.views.content_manager'),
    (r'^cmanager/upload$', 'mypublisher.views.render_upload_content'),
    (r'^cmanager/upload/save$', 'mypublisher.views.save_content'),
    
    
)