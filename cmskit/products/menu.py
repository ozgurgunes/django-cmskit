# -*- coding: utf-8 -*-
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from cmskit.products.models import Product, Category
from menus.base import Modifier
from menus.menu_pool import menu_pool

class ProductsMenu(CMSAttachMenu):

    name = _("Products menu")

    def get_nodes(self, request):
        nodes = []
        for category in Category.objects.select_related().order_by("tree_id", "lft"):
            node = NavigationNode(
                category.title,
                category.get_absolute_url(),
                category.pk,
                category.parent_id
            )
            nodes.append(node)
        for product in Product.objects.published().select_related():
            node = NavigationNode(
                product.title,
                product.get_absolute_url(),
                product.category,
                product.category.pk
            )
            nodes.append(node)

        return nodes
        
#menu_pool.register_menu(ProductsMenu)
