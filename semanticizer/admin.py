from django.contrib.admin import site
from semanticizer.models import *

site.register(DataSetFormat)
site.register(DataSet)
site.register(Semantics)
site.register(SemanticsSpecification)