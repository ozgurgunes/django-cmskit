# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site

def site(request):
    site = Site.objects.get_current()
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', site.name),
        'SITE_DOMAIN': getattr(settings, 'SITE_DOMAIN', site.domain),
    }
