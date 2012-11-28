# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ArticlesApp(CMSApp):
    name = _('Articles App') # give your app a name, this is required
    urls = ['cmskit.articles.urls'] # link your app to url configuration(s)
    
apphook_pool.register(ArticlesApp) # register your app