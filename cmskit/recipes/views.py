# -*- coding: utf-8 -*-
import re
import operator
from django.db import models
from django.views.generic import ListView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from cmskit.recipes.models import Recipe
from cmskit.recipes.forms import RecipeForm
from django.utils import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed

def normalize(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]
    
class RecipeSearch(ListView):
    model = Recipe
    
    def get_queryset(self):
        terms = normalize(self.request.GET.get('s', ''))
        q_objects = []
        
        for term in terms:
            q_objects.append(models.Q(title__icontains=term))
            q_objects.append(models.Q(directions__icontains=term))
            q_objects.append(models.Q(ingredients__icontains=term))
            q_objects.append(models.Q(tags__icontains=term))

        return self.model.objects.published().select_related().filter(reduce(operator.or_, q_objects))

class RecipeForm(CreateView):
    model = Recipe
    form_class = RecipeForm
    
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RecipeForm, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def form_invalid(self, form):
        return HttpResponse('['+json.dumps(form.errors)+']', mimetype='application/json')

    def form_valid(self, form):
        recipe = form.save()
        data = {
            'id'    : recipe.id, 
            'title'  : recipe.title, 
            'ingredients'  : recipe.ingredients, 
            'directions'  : recipe.directions, 
            'picture'  : recipe.picture.url, 
            'date_created'  : recipe.date_created.strftime('%Y-%m-%dT%H:%M:%S')
        }
        return HttpResponse('['+json.dumps(data)+']', mimetype='application/json')
        