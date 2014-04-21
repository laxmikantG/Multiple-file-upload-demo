'''
Created on 08-Feb-2014
@author: laxmikant
'''

class Logging():
    '''  Access Log and Error Log  '''

    def __init__(self):
        '''
            Constructor
        '''
    
    def request_logging(self, request):
        ''' '''
        req_dict = dict(zip(request.GET.keys(),request.GET.values()))
        self.writelog(req_dict)
        return self(req_dict) 
        
    def request_POST_logging(self, request):
        ''' '''
        req_dict = dict(zip(request.POST.keys(),request.POST.values()))
        self.writelog(req_dict)
        return self(req_dict)
    
    def writelog(self, data):
        ''' Write log file '''
        fp = open("/tmp/error_log.log", "w")
        fp.write(str(data))
        fp.close()