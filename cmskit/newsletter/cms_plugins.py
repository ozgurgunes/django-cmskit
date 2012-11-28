# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from cmskit.newsletter.forms import SubscriptionForm


class SubscribeForm(CMSPluginBase):
    model = CMSPlugin
    name = _("Subscribe Form")
    render_template = "newsletter/_form.html"
    
    def render(self, context, instance, placeholder):
        context.update({
                    'form': SubscriptionForm(),
                    'placeholder': placeholder
                })
        return context
        
plugin_pool.register_plugin(SubscribeForm)
