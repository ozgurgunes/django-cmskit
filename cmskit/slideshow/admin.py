# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cmskit.slideshow.forms import AdminSlideWidget
from cmskit.slideshow.models import Slide
from cmskit.utils.admin import OrderableStackedInline


class SlideInline(OrderableStackedInline):

    model = Slide 
    fieldsets = (
            (None, {
                'fields': ('picture', 'url', 'publish', ('date_created', 'date_updated'))
            }),
            (_('Texts'), {
                'classes': ('collapse',),
                'fields': ('title', 'summary', 'alt')
            }),
        )
    readonly_fields = ('date_created', 'date_updated')
          
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            kwargs.pop('request', None)
            kwargs['widget'] = AdminSlideWidget
            return db_field.formfield(**kwargs)
        return super(SlideInline, self).\
            formfield_for_dbfield(db_field, **kwargs)
            
# class SlideAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slideshow', 'publish']
#     
# admin.site.register(Slide, SlideAdmin)
# 