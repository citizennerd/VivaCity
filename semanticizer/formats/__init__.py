from abc import *
import tempfile
from distutils.file_util import write_file
import urllib2

class BaseFormatter(object):
    __metaclass__ = ABCMeta
    
    def get_file(self, url):
        response = urllib2.urlopen(url)
        return response.read()        
    
    @abstractmethod
    def extract_columns(self, file, **kwargs):
        return []
   
    @abstractmethod
    def to_dict(self, file, transformation):
        return {}
        
def do_transformation(s, trans):
    status = s
    operations  = trans.split('.')
    for operation in operation:
        args = operation.split('(')[1].split(")")[0].split(",")
        if operation.startswith('on_longer_than'):
            status = [s for s in status if len(s) > int(args[0])]
        if operation.startswith('on_shorter_than'):
            status = [s for s in status if len(s) < int(args[0])]
        if operation.startswith('on_exact_length'):
            status = [s for s in status if len(s) == int(args[0])]
        if operation.startswith('on_contains'):
            status = [s for s in status if s.contains(args[0])]
        if operation.startswith('on_startswith'):
            status = [s for s in status if s.startswith(args[0])]
        if operation.startswith('on_endswith'):
            status = [s for s in status if s.endswith(args[0])]
        if operation.startswith('on_isdigit'):
            status = [s for s in status if s.isdigit()]
        if operation.startswith('on_islower'):
            status = [s for s in status if s.islower()]
        if operation.startswith('split'):
            status = status.split(args[0])
        if operation.startswith('get'):   
            status = [status[i] for i in args]
        if operation.startswith('upper'):   
            status = [s.upper() for s in status]
        if operation.startswith('lower'):   
            status = [s.lower() for s in status]
        if operation.startswith('strip'):   
            status = [s.strip() for s in status]
    return " ".join(status)