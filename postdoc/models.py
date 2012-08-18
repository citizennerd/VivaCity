from django.db import models
from django.contrib.gis.db import models as gmodels

class DataModel(models.Model):
    name = models.CharField(max_length=255)
    super = models.ForeignKey('DataModel', blank=True, null=True)
    is_base = models.BooleanField(default=False)
    geo_representation = models.CharField(max_length=100, blank=True, null=True)
    container = models.ForeignKey('DataModel', blank=True, null=True, related_name="contains")
    concept = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class DataModelAttribute(models.Model):
    model = models.ForeignKey(DataModel, related_name="attributes")
    name = models.CharField(max_length=255)
    data_type = models.ForeignKey(DataModel)
    
    def __str__(self):
        return self.name
    
class DataInstance(models.Model):
    data_type = models.ForeignKey(DataModel, related_name = "instances")
    geometry = gmodels.GeometryCollectionField(null=True, blank=True)
    
    def __str__(self):
        return "%s:%s" % (self.data_type, self.id, )
    
class DataInstanceAttribute(models.Model):
    instance = models.ForeignKey(DataInstance, related_name="attributes")
    attribute = models.ForeignKey(DataModelAttribute)
    value = models.TextField()
    
    