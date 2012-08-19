from abc import *
import tempfile
from distutils.file_util import write_file
import urllib2

from django.utils import importlib

def get_adapter(name):
    package = "semanticizer.formats."+name
    klass = "Formatter"

    # dynamically import the module, in this case app.backends.adapter_a
    module = importlib.import_module(package)

    # pull the class off the module and return
    return getattr(module, klass)
 

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

def multi_split(s, seps):
    res = [s]
    for sep in seps:
        s, res = res, []
        for seq in s:
            res += seq.split(sep)
    return res
      
def do_transformation(s, trans):
    status = s
    operations  = trans.split('.')
    for operation in operations:
        if operation.strip() != "":
            args = operation.split('(',1)[1].rsplit(")",1)[0].split(",")
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
                for i in range(0,len(args)):
                    if args[i] == '" "':
                        args.append(" ")
                        args.append("\n")
                        args.append("\t")
                        args.append("\r")
                status = multi_split(status, args)
            if operation.startswith('get'):   
                status = [status[int(i)] for i in args]
            if operation.startswith('upper'):   
                status = [s.upper() for s in status]
            if operation.startswith('lower'):   
                status = [s.lower() for s in status]
            if operation.startswith('strip'):   
                status = [s.strip() for s in status]
            if operation.startswith('prepend'):   
                status = args[0]+status
            if operation.startswith('append'):   
                status = status + args[0]
            if operation.startswith('replace'):   
                for i in range(0, len(args)):
                    args[i] = args[i].replace("\"","")
                status = status.replace(args[0],args[1])
    if isinstance(status, type([])):
        return " ".join(status)
    return status

