# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from cmskit.recipes.models import Recipe

class RecipesMenu(CMSAttachMenu):

    name = _("Recipes menu")

    def get_nodes(self, request):
        nodes = []
        for recipe in Recipe.objects.published().select_related():
            try:
                node = NavigationNode(
                    recipe.title,
                    recipe.get_absolute_url(),
                    recipe.pk
                )
                nodes.append(node)
            except:
                pass
            
        return nodes
        
menu_pool.register_menu(RecipesMenu)
