# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from cmskit.slideshow.models import Slideshow
from cmskit.slideshow.admin import SlideInline


class SlideshowPlugin(CMSPluginBase):
    model = Slideshow
    inlines = (SlideInline,)
    name = _("Slideshow")
    render_template = "slideshow/_slideshow.html"
    
    def render(self, context, instance, placeholder):
        context.update({
                    'slides': instance.slide_set.published().select_related().filter(publish=True), 
                    'placeholder':placeholder
                })
        return context    
        
plugin_pool.register_plugin(SlideshowPlugin)
