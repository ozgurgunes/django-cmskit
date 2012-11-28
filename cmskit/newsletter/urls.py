from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('cmskit.newsletter.views',

    url(r'^export-csv/$',
        'export_csv',
        name='export_csv',
    ),

    url (r'^$', 
        'subscribe_detail',
        name='subscribe_detail',
    ),

)