# -*- coding: utf-8 -*-
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmskit.products.models import Product, ProductTeaserPlugin


class ProductTeaser(CMSPluginBase):
    model = ProductTeaserPlugin
    name = _('Product Teaser')
    render_template = "products/_teaser.html"

    def render(self, context, instance, placeholder):
        
        if instance.product:
            product = instance.product
        else:
            products = Product.objects.published().select_related().order_by('?')
            if instance.category:                
                products = products.filter(
                                Q(category=instance.category) | 
                                Q(category__parent=instance.category))
            try:
                product = products[0]
            except:
                product = ''
            
        context.update({
                    'product': product,
                    'placeholder':placeholder
                })
        return context    
        
plugin_pool.register_plugin(ProductTeaser)
