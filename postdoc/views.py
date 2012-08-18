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
    for attribute in di.attributes.all():
        jdia = {}
        jdia['id'] = attribute.attribute.id
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
        
    if dm.contains.count()>0:
        jdm['contains']=[]
        for conainee in dm.contains.all():
            jdmc = {}
            jdmc['data_type'] = containee.name
            jdmc['data_type_id'] = containee.id
    jdm['is_base'] = dm.is_base
    jdm['geo_representation'] = dm.geo_representation
    jdm['abstract'] = dm.abstract
    jdm['attributes'] = []
    for attribute in dm.attributes.all():
        jdma = {}
        jdma['name'] = attribute.name
        jdma['id'] = attribute.id
        jdma['data_type'] = attribute.data_type.name
        jdma['data_type_id'] = attribute.data_type.id
        jdm['attributes'].append(jdma)
    
    return jdm

def get_visible_models():
    tldms = DataModel.objects.filter(container__isnull = True)
    dms = []
    for tldm in tldms:
        dms.append({"name":tldm.name, "id":tldm.id, 'url':""})
    return dms
        
    
def get_visible_instances():
    tldmis = DataModelInstance.objects.filter(data_type__container__isnull=True)
    dmis = []
    for tldmi in tldmis:
        dmis.append({'id':tldmi.id, 'geometry':tldmi.geometry.geojson, 'url':""})
    

def http_get_data_json(request, id):
    return HttpResponse(json.dumps(get_data_json(id)), content_type="text/json")

def http_get_instance_json(request, id):
    return HttpResponse(json.dumps(get_instance_json(id)), content_type="text/json")

def http_get_visible_models(request):
    return HttpResponse(json.dumps(get_visible_models()), content_type="text/json")
            