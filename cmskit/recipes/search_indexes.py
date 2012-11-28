# -*- coding: utf-8 -*-
import datetime
from haystack.indexes import *
from haystack import site
from cmskit.recipes.models import Recipe
from cms_search.search_helpers.indexes import MultiLanguageIndex

class RecipeIndex(MultiLanguageIndex):
    title   = CharField(model_attr='title')
    url     = CharField(stored=True)
    text    = CharField(document=True, use_template=True, 
                    template_name='search/recipes/recipe_index.txt')

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Recipe.objects.published().select_related()
        
    def prepare_url(self, obj):
        try:
            return obj.get_absolute_url()
        except:
            pass
        
    class HaystackTrans:
        fields = ('url',)

site.register(Recipe, RecipeIndex)

