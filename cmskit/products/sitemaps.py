# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.utils.translation import activate, deactivate
from cmskit.products.models import Product

class ProductsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        #return Product.objects.published().select_related()
        items = []
        for lang in dict(settings.LANGUAGES).keys():
            activate(lang)
            for p in Product.objects.translation(lang).published():
                items.append({
                    'lang': lang,
                    'url': p.get_absolute_url(),
                    'date': p.date_updated
                })
        deactivate()
        return items

    def location(self, obj):
        return '/' + obj['lang'] + obj['url']

    def lastmod(self, obj):
        return obj['date']