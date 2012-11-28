# -*- coding: utf-8 -*-
from django.forms import ModelForm, Field, CharField, HiddenInput
from django.forms.util import ErrorList
from django.core.exceptions import ValidationError
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from models import Contact


class KeyField(CharField):

    def validate(self, value):
        # valdates always. validation is done in the form (see below)
        pass


class ContactAdminForm(ModelForm):

    akismet_api_key         = KeyField(_("Akismet API Key"),
                                help_text=_('Get a Wordpress Key from http://akismet.com/'))
    recaptcha_public_key    = KeyField(_("ReCAPTCHA Public Key"),
                                help_text=_('Get this from http://www.google.com/recaptcha'))
    recaptcha_private_key   = KeyField(_("ReCAPTCHA Private Key"),
                                help_text=_('Get this from http://www.google.com/recaptcha'))
    
    class Meta:
        model = Contact
        
    def _add_error(self, field_name, error):
        if not field_name in self._errors:
            self._errors[field_name] = ErrorList()
        self._errors[field_name].append(error)
    
    def _check_akismet(self):

        try:
            from akismet import Akismet
            api_key = getattr(settings, "AKISMET_API_KEY", 
                        self.cleaned_data['akismet_api_key'])        
            if not hasattr(settings, "AKISMET_API_KEY"):
                if not api_key:
                    self._add_error('akismet_api_key', Field.default_error_messages['required'])
                else:
                    ak = Akismet(
                        key = api_key,
                        blog_url = 'http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
                    )
                    if not ak.verify_key():
                        self._add_error('akismet_api_key', _('The API Key is not valid.'))
        except ImportError:
           self._add_error('spam_protection_method', _('Akismet library is not installed.'))        
                   
    
    def _check_recaptcha(self):
            
        try:
            from recaptcha.client import captcha as recaptcha
            public_key = getattr(settings, "RECAPTCHA_PUBLIC_KEY", 
                         self.cleaned_data['recaptcha_public_key'])
            private_key = getattr(settings, "RECAPTCHA_PRIVATE_KEY", 
                          self.cleaned_data['recaptcha_private_key'])

            if not public_key:
                self._add_error('recaptcha_public_key', Field.default_error_messages['required'])
            if not private_key:
                self._add_error('recaptcha_private_key', Field.default_error_messages['required'])
        except ImportError:
            self._add_error('spam_protection_method', _('ReCAPTCHA library is not installed.'))
            
            
    
    def clean(self):
        
        method = self.cleaned_data['spam_protection_method']
        if method == 1:
            # user chose aksimet => akismet api key is required
            self._check_akismet()
        elif method == 2:
            # user chose recaptcha => recaptcha keys are required
            self._check_recaptcha()
        
        return self.cleaned_data

