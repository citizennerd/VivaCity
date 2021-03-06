from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # main page
    url(r'^$', 'ui.views.index', name='home'),
    url(r'^uth$', 'ui.views.uth', name='uth'),
    url(r'^external/(?P<path>.*)$', 'ui.views.proxy', name="proxy"),

    #data urls
    url(r'^data/instances/(?P<id>\d+)$', 'postdoc.views.http_get_instance'),
    url(r'^data/instances/visible$', 'postdoc.views.http_get_visible_instances'),
    url(r'^data/instances/all$', 'postdoc.views.http_get_all_instances'),
    
    url(r'^data/instances/type$', 'postdoc.views.http_get_typed_instances'),
    
    
    url(r'^data/models/(?P<id>\d+)$', 'postdoc.views.http_get_data'),
    url(r'^data/models/visible$', 'postdoc.views.http_get_visible_models'),
    url(r'^data/models.json$', 'postdoc.views.get_models'),
    url(r'^data/models/viewer$', 'postdoc.views.models_index'),
    
    url(r'^data/import/(?P<id>\d+)$', 'postdoc.views.store'),

    #semantics urls
    url(r'^semantics/fetch/(?P<id>\d+)$', 'semanticizer.views.fetch_data', name="fetch"),
    url(r'^semantics/datasets.json$', 'semanticizer.views.get_datasets', name="step_1"),
    
    #admin (cuz we all luv dj)!!!
    url(r'^admin/', include(admin.site.urls)),

)

# ... the rest of your URLconf goes here ...
urlpatterns += staticfiles_urlpatterns()