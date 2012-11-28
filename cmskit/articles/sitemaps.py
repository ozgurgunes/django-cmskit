# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from cmskit.articles.models import Article

class ArticlesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Article.objects.published().select_related()

    def location(self, obj):
        plugin = obj.index.articleindex_set.all()[0]
        return u'/%s%s%s/%s' % (plugin.language, obj.index.page.get_absolute_url(), obj.slug, obj.pk)

    def lastmod(self, obj):
        return obj.date_updated