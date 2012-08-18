from django.http import HttpResponse

from postdoc.models import *

import json

def get_instance_json(instance_id):
    di = DataInstance.objects.get(id=instance_id)
    jdi = {}
    jdi['id'] = di.id
    jdi['data_type'] = di.data_type.name
    jdi['data_type_id'] = di.data_type.id
    if di.geometry is not None and di.geometry != "":
        jdi['geometry'] = di.geometry.geojson(); 
    jdi['attributes'] = []
    for attribute in di.attributes:
        jdia = {}
        jdia['name'] = attribute.attribute.name
        jdia['data_type'] = attribute.attribute.data_type.name
        jdia['data_type_id'] = attribute.attribute.data_type.id
        jdia['value'] = attribute.attribute.value
        jdi['attributes'].append(jdia)
    return jdi
    
def get_data_json(datamodel_id):
    dm = DataModel.objects.get(id=datamodel_id)
    jdm = {}
    
    jdm['name'] = dm.name
    jdm['id'] = dm.id
    if dm.super is not None:
        jdm['super'] = dm.super.name
        jdm['super_id'] = dm.super.id
    jdm['is_base'] = dm.is_base
    jdm['geo_representation'] = dm.geo_representation
    jdm['abstract'] = dm.abstract
    jdm['attributes'] = []
    for attribute in dm.attributes:
        jdma = {}
        jdma['name'] = attribute.name
        jdma['data_type'] = attribute.data_type.name
        jdma['data_type_id'] = attribute.data_type.id
        jdm['attributes'].append(jdma)
    
    return jdm


def http_get_data_json(request, id):
    return HttpResponse(json.dumps(get_data_json(id)), content_type="text/json")

def http_get_instance_json(request, id):
    return HttpResponse(json.dumps(get_instance_json(id)), content_type="text/json")