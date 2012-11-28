from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models import get_model
from django.template.defaultfilters import slugify
from cmskit.newsletter.models import Subscription
from cmskit.newsletter.forms import SubscriptionForm
from cmskit.newsletter.core import csv

import datetime
import re
import csv

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def export_csv(request, model=Subscription):
    """
    Generic CSV export. Thanks to:
    http://www.djangosnippets.org/snippets/591/
    """
    if model.objects.all():
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(model.__name__)
        writer = csv.writer(response)
        # Write headers to CSV file
        headers = []
        for field in model._meta.fields:
            headers.append(field.name)
        writer.writerow(headers)
        # Write data to CSV file
        print model.objects.all()
        for obj in model.objects.all().order_by("id"):
            row = []
            for field in model._meta.fields:
                row.append(getattr(obj, field.name))
            writer.writerow(row)
        # Return CSV file to browser as download
        return response
    else:
        request.user.message_set.create(message=_('There are no emails in the database.'))
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

def subscribe_detail(request, form_class=SubscriptionForm, 
        template_name='newsletter/subscribe.html',  
        success_template='newsletter/success.html', extra_context={}, 
        model_str="newsletter.subscription"):
    
    '''
    TODO:
    '''
    
    if request.POST:   
        form = form_class(request.POST)
        
        if form.is_valid():
            
            subscribed = form.cleaned_data["subscribed"]
            email = form.cleaned_data["email"]
            subscription = None
            model = None
            try:
                """
                if the user already exists we're just gonna update
                otherwise the form, as is, will throw an exception
                if the unique email already exists.
                """
                
                model = get_model(*model_str.split('.')) 
                subscription = model._default_manager.get(email=email)    
                subscription.subscribed = subscribed
                subscription.save()
            except (AttributeError, model.DoesNotExist):
                #contiue on processing
                pass
            
            message = getattr(settings,
                "NEWSLETTER_OPTIN_MESSAGE", "Success! You've been added.")
            
            #if opt-out
            if not subscribed:
                message = getattr(settings,
                     "NEWSLETTER_OPTOUT_MESSAGE", 
                     "You've been removed. Sorry to see ya go.")          
            
            #ok so this is a new signup, save()
            if not subscription:
                form.save()

            extra = {
                'success': True,
                'message': message,
                'form': form_class(),
            }
            extra.update(extra_context)
            
            return render_to_response(success_template, extra, 
                 RequestContext(request))
    else:
        form = form_class()
    
    extra = {
        'form': form,
    }
    extra.update(extra_context)

    if request.is_ajax():
        template_name = template_name[:-5]+'_ajax.html'
    
    return render_to_response(template_name, extra, RequestContext(request))

