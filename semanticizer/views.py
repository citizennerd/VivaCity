from django.http import HttpResponse

from semanticizer.forms import * 

def step_1(request):
    form = DataSetForm()
    return HttpResponse