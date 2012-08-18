from django.http import HttpResponse
from django.core.urlresolvers import reverse

from semanticizer.forms import * 
from semanticizer.formats import * 
from semanticizer.models import * 

import json

def fetch_data(request,id):
    ds = DataSet.objects.get(id=id)
    model = ds.format.module
    fmat = get_adapter(model)()
    
    transform = {}
    for semantic in ds.semantics.all():
        for spec in semantic.associations.all():
            transform[spec.column] = []
            tsc = {}
            tsc['target'] = spec.attribute.id
            tsc['op'] = spec.data_transformation
            transform[spec.column].append(tsc)
    data = fmat.to_dict(ds.file, transform)
    return HttpResponse(json.dumps(data))
    

def step_1(request):
    if request.method == "GET":
        form = DataSetForm()
        data = {
            'form':form.as_p(),
            'url':reverse('step_1')
        }
        return HttpResponse(json.dumps(data))
    else:
        dataset = DataSetForm(request.POST)
        dataset.save()
        form = SemanticsForm()
        data = {
            'form':form.as_p(),
            'url':reverse('step_2')
        }
        return HttpResponse(json.dumps(data))
    
def step_2(request):
    if request.method == "GET":
        form = SemanticsForm()
        data = {
            'form':form.as_p(),
            'url':reverse('step_2')
        }
        return HttpResponse(json.dumps(data))
    else:
        dataset = SemanticsForm(request.POST)
        dataset.save()
        form = SemanticsSpecificationForm()
        data = {
            'form':form.as_p(),
            'url':reverse('step_3')
        }
        return HttpResponse(json.dumps(data))
    
def step_3(request):
    if request.method == "GET":
        form = SemanticsForm()
        data = {
            'form':form.as_p(),
            'url':reverse('step_3')
        }
        return HttpResponse(json.dumps(data))
    else:
        dataset = SemanticsForm(request.POST)
        dataset.save()
        return HttpResponse("ok")
        