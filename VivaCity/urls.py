from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # main page
    url(r'^$', 'ui.views.index', name='home'),

    #data urls
    url(r'^data/instances/(?<id>\d+)$', 'postdoc.views.http_get_instance'),
    url(r'^data/models/(?<id>\d+)$', 'postdoc.views.http_get_data'),
    
    url(r'^data/instances/visible$', 'postdoc.views.http_get_visible_instances'),
    url(r'^data/models/visible$', 'postdoc.views.http_get_visible_models'),

    #semantics urls
    url(r'^semantics/add/step_1$', 'semanticizer.views.step_1', name="step_1"),
    url(r'^semantics/add/step_2$', 'semanticizer.views.step_2', name="step_2"),
    url(r'^semantics/add/step_3$', 'semanticizer.views.step_3', name="step_3"),

    #admin (cuz we all luv dj)!!!
    #url(r'^admin/', include(admin.site.urls)),
)
