# -*- coding: utf-8 -*-
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin

from cmskit.gallery.models import Image
from cmskit.gallery.forms import Gallery, AdminImageWidget, GalleryForm
from cmskit.utils.admin import OrderableStackedInline


class ImageInline(OrderableStackedInline):

    model = Image

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'src':
            kwargs.pop('request', None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageInline, self).\
            formfield_for_dbfield(db_field, **kwargs)

            
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    form = GalleryForm
    inlines = (ImageInline, )

admin.site.register(Gallery, GalleryAdmin)
