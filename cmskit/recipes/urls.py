# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView

from cmskit.recipes.models import Recipe
from cmskit.recipes.views import RecipeSearch, RecipeForm

urlpatterns = patterns('',

    url(r'^$', 
        ListView.as_view(model=Recipe, template_name='recipes/index.html'),
        name='recipes_index'),

    url(r'^search/$', 
        RecipeSearch.as_view(template_name='recipes/index.html'),
        name='recipes_search'),

    url(r'^create/$', 
        RecipeForm.as_view(template_name='recipes/form.html'),
        name='recipes_form'),

    url(r'^(?P<slug>[-\w]+)/$', 
        DetailView.as_view(model=Recipe, template_name='recipes/recipe.html'),
        name='recipes_recipe'),
        
)