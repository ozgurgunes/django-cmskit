# -*- coding: utf-8 -*-
from django.utils.translation import get_language
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import Http404
from cmskit.products.models import Category, Product

def index(request):
    categories = Category.objects.select_related().filter(parent=None)
    return render_to_response('products/index.html', {'categories': categories},
                context_instance=RequestContext(request))
 
def detail(request, path, *args, **kwargs):
    slugs = path.split('/')

    try:
        query = Product.objects.published().select_related()
        product = eval('query.get('
                    'slug_'+get_language()+'=slugs[-1],' 
                    'category__slug_'+get_language()+'=slugs[-2])')
        return render_to_response('products/product.html', {'product':product}, 
                    context_instance=RequestContext(request))
    except: pass
    
    query = Category.objects.select_related().all()
    category = eval('get_object_or_404(query,'
                    'slug_'+get_language()+'=slugs[-1])')
    return render_to_response('products/category.html', {'category':category}, 
                    context_instance=RequestContext(request))
        
    