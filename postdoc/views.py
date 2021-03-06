from django.http import HttpResponse
from django.shortcuts import render_to_response

from postdoc.models import *
from postdoc.ops import do_store
import json
import urllib2
from django.contrib.gis.geos import Polygon, Point
from django.contrib.gis.measure import D

from semanticizer.views import do_fetch_data_id


def get_instance_json_id (instance_id, flatten=False):
    di = DataInstance.objects.get(id=instance_id)
    return get_instance_json(di,False,flatten)

def get_instance_json(di, avoid_geo = False, flatten=False):
    jdi = {}
    if di.get_geometry is not None and not avoid_geo:
        jdi['type'] = "Feature"
    jdi['id'] = di.id
    jdi['data_type'] = di.data_type.name
    jdi['data_type_id'] = di.data_type.id
    if di.get_geometry is not None and not avoid_geo:
        jdi['geometry'] = json.loads(di.get_geometry.geojson); 
    jdi['properties'] = {}
    for attribute in di.attributes.all():
        jdia = {}
        jdia['parent_data_type'] = di.data_type.name
        jdia['parent_type_id'] = di.data_type.id
        jdia['id'] = attribute.attribute.id
        jdia['name'] = attribute.attribute.name
        jdia['data_type'] = attribute.attribute.data_type.name
        jdia['is_base'] = attribute.attribute.data_type.is_base        
        jdia['data_type_id'] = attribute.attribute.data_type.id
        if flatten and attribute.attribute.data_type.is_base == False:
            try:
                jdia['value'] = get_instance_json_id(int(attribute.value))
            except:
                jdia['value'] = attribute.value
        else:
            jdia['value'] = attribute.value
        jdi['properties'][jdia['name']] = jdia
    return jdi

    
def get_data_json_id(datamodel_id):
    dm = DataModel.objects.get(id=datamodel_id)
    return get_data_json(dm)
    
def get_data_json(datamodel):
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
        jdm['contains'].append(jdmc)
    jdm['is_base'] = dm.is_base
    jdm['geo_representation'] = dm.geo_representation
    jdm['attributes'] = []
    for attribute in dm.all_attributes():
        jdma = {}
        jdma['name'] = attribute.name
        jdma['full_name'] = str(attribute)
        jdma['id'] = attribute.id
        jdma['data_type'] = attribute.data_type.name
        jdma['data_type_id'] = attribute.data_type.id
        jdm['attributes'].append(jdma)
    jdm['tags']= []
    for tag in dm.tags.all():
        jdmt = {}
        jdmt['name'] = tag.tag.name
        jdm['tags'].append(jdmt)
    
    return jdm

def get_visible_models():
    tldms = DataModel.objects.filter(container__isnull = True)
    dms = []
    for tldm in tldms:
        dms.append({"name":tldm.name, "id":tldm.id, 'url':""})
    return dms

def get_visible_instances(BB, offset, mmax):
    dis = {}
    dis['type']="FeatureCollection" 
    dis["features"] = []
    if BB is None:
        queryset = DataInstance.objects.filter(geometry__isnull=False)| DataInstance.objects.filter(mgeometry__isnull=False)
    else:
        bbox = Polygon.from_bbox(BB)
        print bbox
        #   queryset = DataInstance.objects.filter(geometry__isnull=False)| DataInstance.objects.filter(mgeometry__isnull=False)
        queryset = DataInstance.objects.filter(geometry__isnull=False, geometry__contained=bbox)| DataInstance.objects.filter(mgeometry__isnull=False, mgeometry__contained=bbox)
    
    
    for di in queryset[offset:offset+mmax]:
        dis["features"].append(get_instance_json(di))
    return dis      
        
def http_get_all_instances(request):
    mmax = min(400, int(request.REQUEST.get('m', "400")))
    offset = min(0, int(request.REQUEST.get('o', "0")))
    
    dis = []
    for di in DataInstance.objects.all()[offset:offset+mmax]:
        dis.append(get_instance_json(di, True))
    return HttpResponse(json.dumps(dis))


def http_get_typed_instances(request):
    type = request.REQUEST.get('type', None)
    if type is None:
        return HttpResponse(json.dumps("[]"))
    lon = request.REQUEST.get('lon', None)
    if lon is None:
        return HttpResponse(json.dumps("[]"))
    lat = request.REQUEST.get('lat', None)
    if lat is None:
        return HttpResponse(json.dumps("[]"))
    p = Point(float(lon),float(lat))
    dis = []
    for di in DataInstance.objects.filter(data_type__id=type, geometry__distance_lte = (p, D(km=0.2)) )|DataInstance.objects.filter(data_type__id=type, mgeometry__distance_lte=(p, D(km=0.2))):
        dis.append(get_instance_json(di, False, True))
    return HttpResponse(json.dumps(dis), content_type="text/json")
    
    
def store(request, id):
    data = do_fetch_data_id(id)
    return HttpResponse(json.dumps(do_store(data)))

def http_get_data(request, id):
    return HttpResponse(json.dumps(get_data_json(id)), content_type="text/json")

def http_get_instance(request, id):
    return HttpResponse(json.dumps(get_instance_json_id(id)), content_type="text/json")

def http_get_visible_models(request):
    return HttpResponse(json.dumps(get_visible_models()), content_type="text/json")

def http_get_visible_instances(request):
    mmax = min(400, int(request.REQUEST.get('m', "800")))
    offset = min(0, int(request.REQUEST.get('o', "0")))
    BB = request.REQUEST.get("BB", None)
    if BB is not None:
        BB = [float(bb) for bb in BB.split(",")]
    return HttpResponse(json.dumps(get_visible_instances(BB,offset,mmax)), content_type="text/json")

def do_get_tags(request):
    return HttpResponse(json.dumps(get_tags(DataTags.objects.filter(super__isnull=True))))

def get_tags(container):
    menu = []
    for tag in container.all(): 
        menu.append({
                     'name':tag.name,
                     'id':tag.id,
                     'description':tag.description,
                     'children':get_tags(tag.subtags) 
                     })
    return menu


def get_models(request):
    nodes = []
    edges = []
    for model in DataModel.objects.filter(is_base=False):
        nodes.append({
                      "id":model.id,
                      'name':model.name,
                      'super':str(model.super),
                      'geo_representation':model.geo_representation,
                      'container':str(model.container),
                      'concept':str(model.concept),
                      'attributes':[{'n':att.name, 't':str(att.data_type),'t_id':att.data_type.id} for att in model.attributes.all()]
                      })
        if model.super is not None:
            edges.append({
                          'from':model.id,
                          'to':model.super.id,
                          'type':"extends"})
        if model.container is not None:
            edges.append({
                          'from':model.id,
                          'to':model.container.id,
                          'type':"contained_in"})
        for att in model.attributes.all():
            edges.append({
                          'from':att.model.id,
                          'to':att.data_type.id,
                          'type':"attribute",
                          'attribute':att.name})
            
    return HttpResponse(json.dumps({'nodes':nodes, 'edges':edges}))

    
def models_index(request):
    return render_to_response('modeler.html')