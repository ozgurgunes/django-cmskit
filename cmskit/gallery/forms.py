# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget

from cmskit.gallery.models import Gallery

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u'<a href="%s" target="_blank">\
                <img src="%s" alt="%s" style="height: 100px;" /></a><br /> %s ' % \
                (unicode(image_url), unicode(image_url), unicode(file_name), _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
        

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
     
    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        choices = [self.fields['page'].choices.__iter__().next()]
        for page in self.fields['page'].queryset:
            choices.append(
                (page.id, ''.join(['- '*page.level, page.__unicode__()]))
            )
        self.fields['page'].choices = choices