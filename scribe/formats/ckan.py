from abc import *
import os
import tempfile
from distutils.file_util import write_file
import urllib2
from scribe.formats import BaseDMS
from django.utils import importlib
import json

#ckan format

class DMSFormat(object):
	def __init__(self, base_url):
		self.base_url = base_url

	def get_datasets(self):
		url = self.base_url + "/api/rest/dataset"
		data = urllib2.urlopen(url).read()
		return json.loads(data)

	def get_dataset(self, dataset_id):
		url = self.base_url + "/api/rest/dataset/"+dataset_id
		data = urllib2.urlopen(url).read()
		data = json.loads(data)

		return data
		

