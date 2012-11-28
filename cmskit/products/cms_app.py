# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from cmskit.products.menu import ProductsMenu

class ProductsApp(CMSApp):
    name = _("Products App") # give your app a name, this is required
    urls = ["cmskit.products.urls"] # link your app to url configuration(s)
    menus = [ProductsMenu]
    
apphook_pool.register(ProductsApp) # register your app