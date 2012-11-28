# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from cmskit.recipes.models import Recipe

class RecipesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        items = []
        for r in Recipe.objects.published().select_related():
            try:
                items.append({
                    'url': r.get_absolute_url(),
                    'date': r.date_updated
                })
            except:
                pass
        return items
        return Recipe.objects.published().select_related()
        
    def location(self, obj):
        return '/' + settings.LANGUAGES[0][0] + obj['url']
        
    def lastmod(self, obj):
        return obj['date']