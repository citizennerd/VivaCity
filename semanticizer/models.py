from django.db import models

from postdoc.models import *

class DataSetFormat(models.Model):
    name = models.CharField(max_length=30)
    module = models.CharField(max_length=100)
    configuration_requirements = models.TextField()
    def __str__(self):
        return self.name    
    
class DataSet(models.Model):
    file = models.URLField()
    format = models.ForeignKey(DataSetImportMethod)
    format_configuration = models.TextField()
    refresh_period = models.TextField()
    def __str__(self):
        return self.file    
    
class Semantics(models.Model):
    dataset = models.ForeignKey(DataSet, related_name="semantic")
    data_model = models.ForeignKey(DataModel)
    def __str__(self):
        return "%s => %s" % (self.dataset.file, self.data_model.name)    
        
class SemanticsSpecification(models.Model):
    semantics = models.ForeignKey(Semantics, related_name="associations")
    attribute = models.ForeignKey(DataModelAttribute)
    column = models.TextField()
    column_number = models.IntegerField()
    
    data_transformation = models.TextField()
    
    def __str__(self):
        return "%s: %s => %s" % (self.semantics.dataset.file, self.column, self.attribute.name)