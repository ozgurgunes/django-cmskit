# -*- coding: utf-8 -*-
from django.utils.translation import get_language
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import Http404
from django.core.paginator import Paginator

from cmskit.articles.models import Article

def index(request):
    articles = Article.objects.select_related().published()
    return render_to_response('articles/index.html', 
                {'articles': articles}, 
                context_instance=RequestContext(request))


def article(request, slug, pk):
    article = get_object_or_404(Article.objects.published().select_related(),
                        publish=True, slug=slug, pk=pk)
                        
    return render_to_response('articles/article.html', 
                {'article':article}, 
                context_instance=RequestContext(request))
