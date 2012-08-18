from django.contrib.admin import site
from postdoc.models import *

site.register(DataModel)
site.register(DataTag)
site.register(ModelTags)
site.register(DataModelAttribute)
site.register(DataInstance)
site.register(DataInstanceAttribute)