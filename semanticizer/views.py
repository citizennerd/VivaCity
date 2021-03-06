from django.http import HttpResponse
from django.core.urlresolvers import reverse

from semanticizer.forms import * 
from semanticizer.formats import * 
from semanticizer.models import * 

import json



def fetch_data(request,id):

    ds = DataSet.objects.get(id=id)
    meta = do_fetch_data(ds)
    
    return HttpResponse(json.dumps(meta))
    
def do_fetch_data_id(id):
    ds = DataSet.objects.get(id=id)
    meta = do_fetch_data(ds)
    return meta
    
def do_fetch_data(ds):
    model = ds.format.module
    fmat = get_adapter(model)()
    
    meta = {}
    ss = {
          'file':ds.file,
          'format':ds.format.name,
          'format_config_base':ds.format.configuration_requirements,
          'format_config_spec':ds.format_configuration,
          'semantics':[]
            }
    transform = {}
    for semantic in ds.semantics.all():
        sq = {
              'data_model': semantic.data_model.name,
              'data_model_id': semantic.data_model.id
        }
        ss['semantics'].append(sq)
        for spec in semantic.associations.all():
            transform[spec.column] = []
            tsc = {}
            tsc['target'] = spec.attribute.id
            tsc['via'] = spec.via.list_ids if spec.via is not None else None
            tsc['op'] = spec.data_transformation
            tsc['semantics'] = spec.id
            tsc['data_model'] = semantic.data_model.name
            tsc['data_model_id'] = semantic.data_model.id
            transform[spec.column].append(tsc)
        for spec in semantic.geo_associations.all():
            transform[spec.column] = []
            tsc = {}
            tsc['target'] = "GEOMETRY"
            tsc['op'] = spec.data_transformation
            tsc['col_x'] = spec.is_geo_x
            tsc['col_y'] = spec.is_geo_y
            tsc['semantics'] = spec.id
            tsc['data_model'] = semantic.data_model.name
            tsc['data_model_id'] = semantic.data_model.id
            transform[spec.column].append(tsc)
    data, a = fmat.to_dict(ds.file, transform) 
    meta['data'] = data
    meta['dataset'] = ss    
    meta['additional'] = a if a is not None else ""
    return meta
    

def get_datasets(request):
    ret = []
    for ds in DataSet.objects.all():
        ret.append({
                    'file':ds.file,
                    'format':str(ds.format),                    
                    'format_configuration':str(ds.format_configuration),
                    'refresh_period':ds.refresh_period,
                    'columns':[dsc.name for dsc in ds.columns.all()]
                            })
    return HttpResponse(json.dumps(ret))


    