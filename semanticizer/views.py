from django.http import HttpResponse
from django.core.urlresolvers import reverse

from semanticizer.forms import * 

import json

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
        