from . import BaseFormatter, do_transformation, lowercase_rename
from django.contrib.gis import gdal
from django.contrib.gis.gdal import SpatialReference

import json
import tempfile
import zipfile
import os
import StringIO

from lxml import etree as xml

class Formatter(BaseFormatter):
    def extract_columns(self, file):
        return ['Name', 'ID', 'status', 'Total', 'Free', 'tendence', 'lat', 'lng']
   
    def to_dict(self, file, transformation):
        return {}
