# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 
        'cmskit.products.views.index', 
        name='products_index'),

    url(r'^(?P<path>(.*))/$', 
        'cmskit.products.views.detail', 
        name='products_detail'),
        
)