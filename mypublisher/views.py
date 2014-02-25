# '''
# Created on 07-Feb-2014
# 
# @author: laxmikant
# '''
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

from mypublisher.core.utils import Utility as UTILITY
# from mypublisher.app_logging import Logging as LogManager
from mypublisher.content_manager import ContentManager 


#https://docs.djangoproject.com/en/1.2/topics/auth/#other-authentication-sources
#http://stackoverflow.com/questions/9825630/login-required-decorator-in-django-1-1-and-template-name


@login_required
def garbage_stat_info(request):
    template = loader.get_template('stat_info.html')
    context = Context({'is_auth': str(request.user.is_authenticated())})
    return HttpResponse(template.render(context))

@login_required
def stat_info(request):
    return render_to_response('stat_info.html',
        {'is_auth':request.user.is_authenticated()},
        context_instance=RequestContext(request))

@login_required
def mainmenu(request):
    return render_to_response('mainmenu.html',{},
        context_instance=RequestContext(request))

def content_manager(request):
    return render_to_response('cmanager_menu.html',{})


def render_upload_content(request):
    return render_to_response('cmanager_upload.html',{}, context_instance=RequestContext(request))


def save_content(request):
    cmanager  = ContentManager() 
    files = request.FILES.getlist("file_names")
    utils = UTILITY()
    req_dict = utils.get_request_dict(request, "POST") 
    message = cmanager.handle_uploaded_file(files, req_dict)
    
    return render_to_response('cmanager_upload.html',{message}, context_instance=RequestContext(request))


def writelog(data):
    fp = open("/tmp/error_log.log", "w")
    fp.write(str(data))
    fp.close()