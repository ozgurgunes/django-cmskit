# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from cmskit.articles.models import Article, Index

class ArticlesMenu(Menu):

    name = _("Articles Menu")

    def get_nodes(self, request):
        nodes = []

        for article in Article.objects.published().select_related():
            node = NavigationNode(
                article.title,
                article.get_absolute_url(),
                article.pk
            )
            nodes.append(node)
        return nodes
        
#menu_pool.register_menu(ArticlesMenu)
