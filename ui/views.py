from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')
def uth(request):
    return render_to_response('uth.html')

def proxy(request, path):
    import httplib2
    conn = httplib2.Http()
    url = path
    if request.method == 'GET':
        url_ending = '%s?%s' % (url, request.GET.urlencode())
        url = "http://" + url_ending
        response, content = conn.request(url, request.method)
    elif request.method == 'POST':
        url = "http://" + url
        data = request.POST.urlencode()
        response, content = conn.request(url, request.method, data)
    return HttpResponse(content, status = int(response['status']), mimetype = response['content-type'])
    
def get_google_places(request, BB, types):
    return None


