'''
Created on 13-Feb-2014

@author: laxmikant
'''
from mypublisher.core.utils import Utility as UTILITY
from django.conf import settings

class ErrorHandler:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.utils = UTILITY()
        self.config = self.utils.read_config_file(settings.\
                                                           ERROR_CODES_INI)
    def get_error_from_config(self, error_code):
        '''
        '''
        message = None
        for section in self.config.sections():
            message = self.get_error_code(section, error_code)
            return message
        return "Internal server error" 
            
        
    def get_error_code(self, section, error_code):
        writelog((section, "errormsg", error_code))
#         var_x = dir(self.config)
#         error_codes = self.config.get(section, None)
#         return error_codes.get(error_code, None)
    
def writelog(data):
    '''
        Write log file
    '''
    fp = open("/tmp/error_log.log", "a")
    fp.write(str(data))
    fp.close()