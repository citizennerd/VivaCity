from postdoc.models import *
from django.contrib.gis.geos import GEOSGeometry

import json
import itertools
def set_attribute(instance, attribute, value, depth=0,prefer_ids = []):
    dd = depth
    att = DataModelAttribute.objects.get(id=attribute)
    merge_proposals = []
    prefer_ids_inner = prefer_ids
    #do we already have the stuff?
    for dia in DataInstanceAttribute.objects.filter(value=value['value']):
        merge_proposals.append({'new':instance.id, 'old':dia.instance.id})
    #try to put stuff into the element
    if instance.data_type.all_attributes.filter(id=attribute).count()>0:
        dia = DataInstanceAttribute()
        dia.instance = instance
        dia.attribute= att
        dia.value = value['value']
        dia.save()
    #try to put stuff into a sub-element
    else:
        if instance.attributes.filter(value__in = [str(p) for p in prefer_ids_inner]):
            dit = DataInstance.objects.get(id=instance.attributes.get(attribute__id=value['via'][depth]).value)
        else:
            via = DataModelAttribute.objects.get(id=value['via'][depth])
            dit = via.data_type.instantiate()
            prefer_ids_inner.append(dit.id)
            ndma = DataInstanceAttribute()
            ndma.instance = instance
            ndma.attribute = via
            ndma.value=dit.id
            ndma.save()
        
        set_attribute(dit, attribute, value, depth+1, prefer_ids_inner)
#        iis = instance.attributes.filter(attribute__data_type = dma)
#        for i in iis:
#            if i.attributes.filter(attribute__id = attribute, value=value['value']):
#                merge_proposals.append({'new':ni.id, 'old':i.id})
#    else:
#        dms = DataModel.objects.filter(is_base=False, id__in=[i.data_type.id for i in instance.data_type.all_attributes])
    return merge_proposals, prefer_ids_inner

def do_store(data):
    dataset = data['dataset']
    data = data['data']
    ins = 0
    
    add_results = []
    prerferred = []
    for semantic in dataset['semantics']:
        dm = DataModel.objects.get(id=semantic['data_model_id'])
        for row in data:
            instance = dm.instantiate()
            ins += 1
            for att, value in row.items():
                if att == "geo_location":
                    print "GEO!!!"
                    gg = GEOSGeometry(json.dumps(value))
                    if gg.num_geom > 1:
                        instance.geometry = gg
                    else:
                        instance.mgeometry = gg
                else:
                    result, inner = set_attribute(instance, att, value, prefer_ids = prerferred)
                    if len(inner)>0:
                        prerferred.extend(inner)
                        prerferred = list(set(prerferred)) 
                    add_results.append(result)
            instance.save()
    
    return {
            'model_id':dm.id,
            'model':dm.name,
            'inserted':ins,
            'result':add_results
    }
            
    