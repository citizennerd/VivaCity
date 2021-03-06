from django.db import models

from postdoc.models import *
from semanticizer.formats import *

from django.contrib.auth.models import User 

class DataSetFormat(models.Model):
    name = models.CharField(max_length=30)
    module = models.CharField(max_length=100)
    geographic = models.BooleanField()
    configuration_requirements = models.TextField()
    is_api = models.BooleanField(default=False)
    time_explicit = models.BooleanField()
    time_implicit = models.BooleanField()
    def __str__(self):
        return self.name    

class DSFAlias(models.Model):
	name = models.CharField(max_length=255, unique=True)
	dsf = models.ForeignKey(DataSetFormat)
	def __str__(self):
		return "%s => %s" % (self.name, self.dsf)

def create_dataset(structure):
	ds = DataSet()
	file = structure['url']
	if structure['format'] != "" and DSFAlias.objects.filter(name = structure['format']).count() > 0:
		format = DSFAlias.objects.get(name=structure['format'])
    
class DataSet(models.Model):
    owner = models.ForeignKey(User)
    file = models.URLField()
    format = models.ForeignKey(DataSetFormat, null=True, blank=True)
    format_configuration = models.TextField(null=True, blank=True)
    refresh_period = models.TextField(blank = True, null=True)
    private = models.BooleanField(default=False)
    publication_aggregation = models.TextField()
    
    def __str__(self):
        return self.file    
    
    def save(self, *args, **kwargs):
        super(DataSet,self).save()
        
        model = self.format.module
        fmat = get_adapter(model)()
        DataSetColumn.objects.filter(dataset = self).delete()
        for column in fmat.extract_columns(self.file):
            d = DataSetColumn()
            d.dataset = self
            d.name = column
            d.save()
    
        
class DataSetColumn(models.Model):
    dataset = models.ForeignKey(DataSet, related_name="columns")
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        unique_together = ('dataset', 'name')
    
class Semantics(models.Model):
    dataset = models.ForeignKey(DataSet, related_name="semantics")
    data_model = models.ForeignKey(DataModel)
    def __str__(self):
        return "%s => %s" % (self.dataset.file, self.data_model.name)    
        
class SemanticsSpecification(models.Model):
    semantics = models.ForeignKey(Semantics, related_name="associations")
    attribute = models.ForeignKey(DataModelAttribute)
    via = models.ForeignKey('SemanticsSpecificationPath', blank=True, null=True, related_name="path")
    column = models.CharField(max_length=500,blank = True, null=True)
    data_transformation = models.CharField(max_length=200)
    def __str__(self):
        if self.via is not None:
            return "%s: %s => %s via %s" % (self.semantics.dataset.file, self.column, self.attribute.name, self.via)
        return "%s: %s => %s" % (self.semantics.dataset.file, self.column, self.attribute.name)

class SemanticsSpecificationPath(models.Model):
    attribute = models.ForeignKey(DataModelAttribute)
    next = models.ForeignKey('SemanticsSpecificationPath',blank = True, null=True, related_name="previous")
    def __str__(self):
        att = self.next
        li = [str(self.attribute)]
        while att is not None:
            li.append(str(att.attribute))
            att = att.next
        return str(",".join(li)) 
    
    @property
    def list_ids(self):
        att = self.next
        li = [self.attribute.id]
        while att is not None:
            li.append(att.attribute.id)
            att = att.next
        return li


class GeoSemanticsSpecification(models.Model):
    semantics = models.ForeignKey(Semantics, related_name="geo_associations")
    column = models.CharField(max_length=500,blank = True, null=True)
    is_geo_x = models.BooleanField()
    is_geo_y = models.BooleanField()    
    geocode_address = models.BooleanField()
    data_transformation = models.CharField(max_length=200)
    
class TimeSpanType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class TimeSemanticsSpecification(models.Model):
    semantics = models.ForeignKey(Semantics, related_name="time_associations")
    absolute_value = models.DateTimeField(blank=True, null=True)
    column = models.CharField(max_length=500,blank = True, null=True)
    format = models.CharField(max_length=200)
    data_transformation = models.CharField(max_length=200)
    timespan_type = models.ForeignKey(TimeSpanType)
    
    
    
