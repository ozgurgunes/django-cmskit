# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.admin.placeholderadmin import PlaceholderAdmin
from reversion import VersionAdmin

from cmskit.articles.models import Index, Author, Article
from cmskit.articles.forms import IndexForm, ArticleForm


class IndexAdmin(PlaceholderAdmin):
    list_display = ('title',)
    form = IndexForm


class AuthorAdmin(PlaceholderAdmin, VersionAdmin):
    list_display = ('name',)


class ArticleAdmin(PlaceholderAdmin, VersionAdmin):
    list_display = ('title', 'index', 'publish', 'date_published')
    fields = ('index', 'title', 'slug', 'excerpt', 'body', 'picture', 
                ('date_created', 'date_updated'), ('publish', 'date_published'), 
                'top', 'meta', 'media', 'aside', 'bottom')
    readonly_fields = ('date_created', 'date_updated')
    form = ArticleForm
    
    
admin.site.register(Index, IndexAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
