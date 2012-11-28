# -*- coding: utf-8 -*-
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from cmskit.dealers.models import Dealer
from cmskit.dealers.forms import SearchForm

class DealersMapPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Dealers Map")
    render_template = "dealers/_map.html"
    module = _('Dealers')
    
    def render(self, context, instance, placeholder):
        context.update({
                    'dealers': Dealer.objects.published().select_related(), 
                    'placeholder': placeholder
                })
        return context    
        
plugin_pool.register_plugin(DealersMapPlugin)

class DealerLocatorPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Dealer Locator")
    render_template = "dealers/_locator.html"
    module = _('Dealers')
    
    def render(self, context, instance, placeholder):
        context.update({
                    'form': SearchForm(),
                    'placeholder': placeholder
                })
        return context    
        
plugin_pool.register_plugin(DealerLocatorPlugin)
