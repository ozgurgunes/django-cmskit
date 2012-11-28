# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('cmskit.articles.views',

    # url(r'^$', 'index', name='articles_index'),

    url(r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/$', 'article', name='articles_article'),

)