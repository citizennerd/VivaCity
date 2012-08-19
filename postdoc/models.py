from django.db import models
from django.contrib.gis.db import models 

class DataModel(models.Model):
    name = models.CharField(max_length=255)
    super = models.ForeignKey('DataModel', blank=True, null=True)
    is_base = models.BooleanField(default=False)
    geo_representation = models.CharField(max_length=100, blank=True, null=True)
    container = models.ForeignKey('DataModel', blank=True, null=True, related_name="contains")
    concept = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def hierarchy(self):
        list_up_ids = []
        elem = self
        while elem.super != None:
            list_up_ids.append(elem.id)
            elem = elem.super
        list_up_ids.append(elem.id)
        return list_up_ids

    @property
    def all_attributes(self):
        return DataModelAttribute.objects.filter(model__id__in=self.hierarchy())
    
    def instantiate(self):
        i = DataInstance()
        i.data_type = self
        i.save()
        return i
    
class DataTag(models.Model):
    name=models.CharField(max_length=255)
    description = models.TextField()
    super = models.ForeignKey('DataTag', related_name="subtags", blank=True, null=True)
    def __str__(self):
        return self.name

class ModelTags(models.Model):
    data_model = models.ForeignKey(DataModel, related_name="tags")
    tag = models.ForeignKey(DataTag, related_name="models")
    def __str__(self):
        return "%s - %s" % (self.data_model, self.tag, )

class DataModelAttribute(models.Model):
    model = models.ForeignKey(DataModel, related_name="attributes")
    name = models.CharField(max_length=255)
    data_type = models.ForeignKey(DataModel)
    
    def __str__(self):
        return "%s:%s" % (self.model.name, self.name, )
    
class DataInstance(models.Model):
    data_type = models.ForeignKey(DataModel, related_name = "instances")
    geometry = models.GeometryCollectionField(null=True, blank=True)
    
    def __str__(self):
        return "%s:%s" % (self.data_type, self.id, )
    
    def o_value(self):
        names = self.attributes.filter(attribute__name="Name")
        if names.count() == 0:
            return "Object"
        elif names.count() ==1:
            return names[0].value
        else:
            return json.dumps([name.value for name in names])
        
    def o_key (self):
        names = self.attributes.filter(attribute__name="ID")
        if names.count() == 0:
            return self.id
        elif names.count() ==1:
            return names[0].value
        else:
            return json.dumps([name.value for name in names])
        
    
class DataInstanceAttribute(models.Model):
    instance = models.ForeignKey(DataInstance, related_name="attributes")
    attribute = models.ForeignKey(DataModelAttribute)
    value = models.TextField()
    def __str__(self):
        return "%s.%s = %s" % (self.instance, self.attribute.name, self.value )
    
    