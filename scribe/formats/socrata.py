from abc import *
import os
import tempfile
from distutils.file_util import write_file
import urllib2
from scribe.formats import BaseDMS
from django.utils import importlib


#socrata format

class DMSFormat(object):
	def __init__():
		pass	

	def get_datasets(self):
		return []

	def get_dataset(self, dataset_id):
		return {}

