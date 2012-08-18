from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # main page
    # url(r'^$', 'VivaCity.views.home', name='home'),

    #data urls
    url(r'^data/instances/(?<id>\d+)$', 'postdoc.views.http_get_instance'),
    url(r'^data/models/(?<id>\d+)$', 'postdoc.views.http_get_data'),
    
    url(r'^data/instances/visible$', 'postdoc.views.http_get_visible_instances'),
    url(r'^data/models/visible$', 'postdoc.views.http_get_visible_models'),

    #semantics urls
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #admin (cuz we all luv dj)!!!
    url(r'^admin/', include(admin.site.urls)),
)
