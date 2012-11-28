# -*- coding: utf-8 -*-
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from cmskit.articles.models import Article, ArticleIndex, ArticleTeaser


class ArticleIndexPlugin(CMSPluginBase):
    model = ArticleIndex
    name = _("Article Index")
    render_template = "articles/_index.html"
    module = _('Articles')
    
    def render(self, context, instance, placeholder):
        context.update({
                    'articles': instance.index.article_set.published().select_related(), 
                    'page': instance.index.page,
                    'placeholder': placeholder
                })
        return context    
        
plugin_pool.register_plugin(ArticleIndexPlugin)


class LatestArticlesPlugin(CMSPluginBase):
    model = ArticleIndex
    name = _("Latest Articles")
    render_template = "articles/_latest.html"
    module = _('Articles')
    
    def render(self, context, instance, placeholder):
        context.update({
                    'articles': instance.index.article_set.published().select_related(),
                    'page': instance.index.page,
                    'placeholder': placeholder
                })
        return context    
        
plugin_pool.register_plugin(LatestArticlesPlugin)


class ArticleBreadcrumbPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Article Breadcrumb")
    render_template = "articles/breadcrumb.html"
    module = _('Articles')

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(ArticleBreadcrumbPlugin)


class ArticleTeaserPlugin(CMSPluginBase):
    model = ArticleTeaser
    name = _('Article Teaser')
    render_template = "articles/_teaser.html"
    module = _('Articles')

    def render(self, context, instance, placeholder):            
        if instance.article:
            article = instance.article
        else:
            if instance.select == u'random':
                query = Article.objects.published().select_related().order_by('?')
            elif instance.select == u'latest':
                query = Article.objects.order_by('-date_created')
            else:
                query = Article.objects.all()

            if instance.category:                
                query = query.filter(category=instance.category)
            try:
                article = query[0]
            except:
                article = ''
            
        context.update({
                    'article': article,
                    'page': article.index.page,
                    'placeholder':placeholder
                })
        return context    
        
plugin_pool.register_plugin(ArticleTeaserPlugin)
