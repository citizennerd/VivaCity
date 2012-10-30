from abc import *
import os
import tempfile
from distutils.file_util import write_file
import urllib2

from django.utils import importlib

class BaseDMS(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def get_datasets(self):
		return []

	@abstractmethod
	def get_dataset(self, dataset_id):
		return {
			'url':'',
			'format':'',
			'name':''
		}

	def to_semanticizer(self, filter=[]):
		if len(filter) == 0:
			for dataset in self.get_datasets():
				d = self.get_dataset(dataset)
				create_dataset(d)
def get_adapter(name):
    package = "scribe.formats."+name
    klass = "Formatter"

    # dynamically import the module, in this case app.backends.adapter_a
    module = importlib.import_module(package)

    # pull the class off the module and return
    return getattr(module, klass)	
