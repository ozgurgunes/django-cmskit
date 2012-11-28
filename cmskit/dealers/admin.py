# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cmskit.dealers.models import Dealer
from cmskit.dealers.forms import DealerForm


class DealerAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'latitude', 'longitude')
    form = DealerForm
    fields = ('title', 'description', 'picture', 
                ('phone', 'fax'), 'street', ('zipcode', 'city'),
                'country', 'website', ('latitude', 'longitude'),
                'publish', ('date_created', 'date_updated'))
    readonly_fields = ('date_created', 'date_updated')
    
admin.site.register(Dealer, DealerAdmin)
