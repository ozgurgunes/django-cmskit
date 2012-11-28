# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import CharField
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.plugins.text.settings import USE_TINYMCE
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor

from models import Contact
from forms import ContactForm, AkismetContactForm, RecaptchaContactForm, HoneyPotContactForm
from admin import ContactAdminForm

class ContactPlugin(CMSPluginBase):
    model = Contact
    name = _("Contact Form")
    form = ContactAdminForm
    contact_form = ContactForm
    render_template = "contact/contact.html"
    subject_template = "contact/subject.txt"
    email_template = "contact/email.txt"
    
    fieldsets = (
        (None, {
            'fields': ('site_email', 'email_label', 'subject_label', 
                            'content_label', 'thanks', 'submit'),
        }),
        (_('Spam Protection'), {
            'classes': ('collapse',),
            'fields': ('spam_protection_method', 'akismet_api_key', 
                            'recaptcha_public_key', 'recaptcha_private_key', 
                            'recaptcha_theme')
        })
    )
    
    change_form_template = "admin/contact/plugin_change_form.html"

    def get_editor_widget(self, request, plugins):
        """
        Returns the Django form Widget to be used for
        the text area
        """
        if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
            from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
            return TinyMCEEditor(installed_plugins=plugins)
        else:
            return WYMEditor(installed_plugins=plugins)

    def get_form_class(self, request, plugins):
        """
        Returns a subclass of Form to be used by this plugin
        """
        # We avoid mutating the Form declared above by subclassing
        class TextPluginForm(self.form):
            pass
        widget = self.get_editor_widget(request, plugins)
        
        thanks_field = self.form.base_fields['thanks']
        
        TextPluginForm.declared_fields["thanks"] = CharField(widget=widget, 
                                    required=False, label=thanks_field.label, 
                                    help_text=thanks_field.help_text)
        return TextPluginForm


    def get_form(self, request, obj=None, **kwargs):
        plugins = plugin_pool.get_text_enabled_plugins(self.placeholder, self.page)
        form = self.get_form_class(request, plugins)
        kwargs['form'] = form # override standard form
        return super(ContactPlugin, self).get_form(request, obj, **kwargs)

    def create_form(self, instance, request):
        if instance.get_spam_protection_method_display() == 'Akismet':
            AkismetContactForm.aksimet_api_key = instance.akismet_api_key
            class ContactForm(self.contact_form, AkismetContactForm):
                pass
            FormClass = ContactForm
        elif instance.get_spam_protection_method_display() == 'ReCAPTCHA':
            RecaptchaContactForm.recaptcha_public_key = getattr(
                settings, "RECAPTCHA_PUBLIC_KEY",
                instance.recaptcha_public_key)
            RecaptchaContactForm.recaptcha_private_key = getattr(
                settings, "RECAPTCHA_PRIVATE_KEY",
                instance.recaptcha_private_key)
            RecaptchaContactForm.recaptcha_theme = instance.recaptcha_theme
            class ContactForm(self.contact_form, RecaptchaContactForm):
                pass
            FormClass = ContactForm
        else:
            class ContactForm(self.contact_form, HoneyPotContactForm):
                pass
            FormClass = ContactForm
            
        if request.method == "POST":
            return FormClass(request, data=request.POST, files=request.FILES)
        else:
            return FormClass(request)


    def send(self, form, site_email, attachments=None):
        subject = form.cleaned_data['subject']
        if not subject:
            subject = _('No subject')
        email_message = EmailMessage(
            render_to_string(self.subject_template, {
                'subject': subject,
            }).splitlines()[0],
            render_to_string(self.email_template, {
                'data': form.cleaned_data,
            }),
            getattr(settings, 'DEFAULT_FROM_EMAIL', form.cleaned_data['email']),
            [site_email],
            headers = {
                'Reply-To': form.cleaned_data['email']
            },)
        if attachments:
            for var_name, data in attachments.iteritems():
                email_message.attach(data.name, data.read(), data.content_type)
        email_message.send(fail_silently=False)
    
    def render(self, context, instance, placeholder):
        request = context['request']

        form = self.create_form(instance, request)
    
        if request.method == "POST" and form.is_valid():
            self.send(form, instance.site_email, attachments=request.FILES)
            context.update( {
                'contact': instance,
            })
        else:
            context.update({
                'contact': instance,
                'form': form,
            })
            
        return context

    def render_change_form(self, request, context, obj=None, *args, **kwargs):
        context.update({
            'spam_protection_method': obj.spam_protection_method if obj else 0,
            'recaptcha_settings': hasattr(settings, "RECAPTCHA_PUBLIC_KEY"),
            'akismet_settings': hasattr(settings, "AKISMET_API_KEY"),
        })
        
        return super(ContactPlugin, self).render_change_form(request, context, *args, **kwargs)
        
    
plugin_pool.register_plugin(ContactPlugin)