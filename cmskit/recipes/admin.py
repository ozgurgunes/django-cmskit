# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.admin.placeholderadmin import PlaceholderAdmin
from reversion import VersionAdmin

from cmskit.recipes.models import Recipe

class RecipeAdmin(PlaceholderAdmin, VersionAdmin):
    list_display = ('title', 'date_created', 'publish')
    fields = ('title', 'slug', 'ingredients', 'aside', 'directions', 'picture', 
                    ('preperation_time', 'cooking_time'), 'products', 
                    'publish', ('date_created', 'date_updated'),
                    'tags', 'top', 'bottom')
    readonly_fields = ('date_created', 'date_updated')
    
admin.site.register(Recipe, RecipeAdmin)
