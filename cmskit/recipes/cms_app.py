# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from cmskit.recipes.menu import RecipesMenu

class RecipesApp(CMSApp):
    name = _("Recipes App") # give your app a name, this is required
    urls = ["cmskit.recipes.urls"] # link your app to url configuration(s)
    menus = [RecipesMenu]
    
apphook_pool.register(RecipesApp) # register your app
