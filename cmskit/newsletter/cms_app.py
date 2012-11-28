# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class NewsletterApp(CMSApp):
    name = _("Newsletter App") # give your app a name, this is required
    urls = ["cmskit.newsletter.urls"] # link your app to url configuration(s)
    
apphook_pool.register(NewsletterApp) # register your app
