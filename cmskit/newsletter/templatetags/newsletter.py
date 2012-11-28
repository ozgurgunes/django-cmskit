# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from cmskit.newsletter.forms import SubscriptionForm

register = template.Library()

@register.inclusion_tag("newsletter/_form.html")
def subscription_form(*args, **kwargs):
    return {'form': SubscriptionForm() }
