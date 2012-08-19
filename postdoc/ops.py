from postdoc.models import *

def set_attribute(instance, attribute, value):
    merge_proposals = []
    if instance.data_type.all_attributes.filter(id=attribute).count()>0:
        dia = DataInstanceAttribute()
        dia.instance = instance
        dia.attribute__id = attribute
        dia.value = value
        dia.save()
    elif instance.attributes.filter(attribute__data_type = DataModelAttribute.objects.get(id=attribute).model):
        dma = DataModelAttribute.objects.get(id=attribute)
        ni = dma.model.instantiate()
        ndma = DataInstanceAttribute()
        ndma.instance = instance
        ndma.attribute = dma
        ndma.value=ni.id
        iis = instance.attributes.filter(attribute__data_type = dma)
        for i in iis:
            if i.attributes.filter(attribute__id = attribute, value=value):
                merge_proposals.append({'new':ni.id, 'old':i.id})
    else:
        dms = DataModel.objects.filter(is_base=False, id__in=[i.datatype.id for i in instance.data_type.all_attributes])

def do_store(data):
    print "storing data"
    dataset = data['dataset']
    data = data['data']
    ins = 0
    
    add_results = []
    for semantic in dataset['semantics']:
        dm = DataModel.onbjects.get(id=semantic['data_model_id'])
        for row in data:
            instance = dm.instantiate()
            ins += 1
            for att, value in row.items():
                if att == "geo_location":
                    #do shit
                    pass
                else:
                    add_results.append(set_attribute(instance, att, value))
    return {
            'model_id':dm.id,
            'model':dm.name,
            'inserted':ins,
            'result':add_results
    }
            
    