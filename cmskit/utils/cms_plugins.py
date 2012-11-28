# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

class HeaderPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Global Header")
    render_template = "utils/_header.html"
    module = _('Utils')

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(HeaderPlugin)


class FooterPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Global Footer")
    render_template = "utils/_footer.html"
    module = _('Utils')

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(FooterPlugin)


class BreadcrumbPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Breadcrumb")
    render_template = "utils/breadcrumb.html"
    module = _('Utils')

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(BreadcrumbPlugin)


class SubmenuPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Submenu")
    render_template = "utils/submenu.html"
    module = _('Utils')

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(SubmenuPlugin)