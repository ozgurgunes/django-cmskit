# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from django.utils.translation import ugettext_lazy as _
from cmskit.recipes.models import Recipe, RecipeTeaserPlugin

class RecipesWidget(CMSPluginBase):
    model = CMSPlugin
    name = _("Recipe Widget")
    render_template = "recipes/_widget.html"
    module = _('Recipes')
    
    def render(self, context, instance, placeholder):
        return context
        
plugin_pool.register_plugin(RecipesWidget)

class RecipeTeaser(CMSPluginBase):
    model = RecipeTeaserPlugin
    name = _("Recipe Teaser")
    render_template = "recipes/_teaser.html"
    module = _('Recipes')
    
    def render(self, context, instance, placeholder):
        if instance.recipe:
            recipe = instance.recipe
        else:
            recipes = Recipe.objects.published().select_related().order_by('?')
            try:
                recipe = recipes[0]
            except:
                recipe = ''
            
        context.update({
                    'recipe': recipe,
                    'placeholder':placeholder
                })
        return context    

plugin_pool.register_plugin(RecipeTeaser)
