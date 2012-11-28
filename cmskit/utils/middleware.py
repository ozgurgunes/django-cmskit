# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import translation

from cms.middleware.multilingual import MultilingualURLMiddleware
from cms.utils.i18n import get_default_language

class MultilingualMiddleware(MultilingualURLMiddleware):
    """
    Supplies additional method that redirects / to /en /de etc.
    """
    def process_request(self, request):
        #return super(MultilingualMiddleware, self).process_request(request)
        setting = getattr(settings, 'CMS_DEFAULT_LANGUAGE', 'default')
        if setting is 'default':
            language = get_default_language()  
        else:
            language = self.get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = language
        if request.META['PATH_INFO'] == '/' \
            and getattr(settings, 'CMS_SEO_ROOT', True):
            return HttpResponseRedirect('/%s/' % language)