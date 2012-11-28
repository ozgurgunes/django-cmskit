# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('cmskit.dealers.views',

    # url(r'^$', 'index', name='articles_index'),
    url(r'^search/$', 'search', name='dealers_search'),

    url(r'^(?P<pk>\d+)/$', 'dealer', name='dealers_dealer'),

)