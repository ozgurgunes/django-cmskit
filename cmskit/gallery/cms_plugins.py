# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmskit.gallery.models import Gallery, ImageGallery


class GalleryPlugin(CMSPluginBase):

    model   = ImageGallery
    name    = _('Image Gallery')
    render_template = 'gallery/_gallery.html'
    module = _('Gallery')

    def render(self, context, instance, placeholder):
        context.update({
                        'gallery': instance.gallery,
                        'images': instance.gallery.image_set.all(),
                        'page': instance.gallery.page,
                        'placeholder': placeholder
                       })
        return context

plugin_pool.register_plugin(GalleryPlugin)

class GalleryTeaserPlugin(CMSPluginBase):
    model = ImageGallery
    name = _('Gallery Teaser')
    render_template = "gallery/_teaser.html"
    module = _('Gallery')

    def render(self, context, instance, placeholder):
        try:
            image = instance.gallery.image_set.order_by('?')[0]
        except:
            image = ''
        
        context.update({
                    'gallery': instance.gallery,
                    'image': image,
                    'placeholder':placeholder
                })
        return context    
        
plugin_pool.register_plugin(GalleryTeaserPlugin)
