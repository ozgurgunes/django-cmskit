# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class DealersApp(CMSApp):
    name = _("Dealers App") # give your app a name, this is required
    urls = ["cmskit.dealers.urls"] # link your app to url configuration(s)
    
apphook_pool.register(DealersApp) # register your app