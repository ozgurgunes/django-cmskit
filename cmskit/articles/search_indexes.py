# -*- coding: utf-8 -*-
import datetime
from haystack.indexes import *
from haystack import site
from cms_search.search_helpers.indexes import MultiLanguageIndex
from cmskit.articles.models import Article

class ArticleIndex(MultiLanguageIndex):
    title   = CharField(model_attr='title')
    url     = CharField(stored=True)
    text    = CharField(document=True, use_template=True, 
                    template_name='search/articles/article_index.txt')

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Article.objects.published().select_related()
        
    def prepare_url(self, obj):
        return '%s%s/%s' % (obj.index.page.get_absolute_url(), obj.slug, obj.pk)
        
site.register(Article, ArticleIndex)