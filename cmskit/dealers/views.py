# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from cmskit.dealers.models import Dealer


def index(request):
    dealers = Dealer.objects.published().select_related()
    return render_to_response('dealers/index.html', 
                {'dealers': dealers}, 
                context_instance=RequestContext(request))


def search(request):
    dealers = Dealer.objects.published().select_related()
    return render_to_response('dealers/index.html', 
                {'dealers': dealers}, 
                context_instance=RequestContext(request))


def dealer(request, pk):
    dealer = get_object_or_404(Dealer.objects.published().select_related(), 
                        publish=True, pk=pk)
                        
    return render_to_response('dealers/dealer.html', 
                {'dealer': dealer}, 
                context_instance=RequestContext(request))
