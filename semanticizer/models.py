from django.db import models

from postdoc.models import *

class DataSetFormat(models.Model):
    name = models.CharField(max_length=30)
    module = models.CharField(max_length=100)
    geographic = models.BooleanField()
    configuration_requirements = models.TextField()
    def __str__(self):
        return self.name    
    
class DataSet(models.Model):
    file = models.URLField()
    format = models.ForeignKey(DataSetFormat)
    format_configuration = models.TextField()
    refresh_period = models.TextField(blank = True, null=True)
    def __str__(self):
        return self.file    
    
class Semantics(models.Model):
    dataset = models.ForeignKey(DataSet, related_name="semantics")
    data_model = models.ForeignKey(DataModel)
    def __str__(self):
        return "%s => %s" % (self.dataset.file, self.data_model.name)    
        
class SemanticsSpecification(models.Model):
    semantics = models.ForeignKey(Semantics, related_name="associations")
    attribute = models.ForeignKey(DataModelAttribute)
    column = models.CharField(max_length=200,blank = True, null=True)
    column_number = models.IntegerField(blank = True, null=True)
    data_transformation = models.CharField(max_length=200)
    def __str__(self):
        return "%s: %s => %s" % (self.semantics.dataset.file, self.column, self.attribute.name)

class GeoSemanticsSpecification(models.Model):
    semantics = models.ForeignKey(Semantics, related_name="geo_associations")
    column = models.CharField(max_length=200, null=True, blank=True)
    column_number = models.IntegerField(null=True, blank=True)
    is_geo_x = models.BooleanField()
    is_geo_y = models.BooleanField()    
    data_transformation = models.CharField(max_length=200)
    