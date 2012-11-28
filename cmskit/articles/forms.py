# -*- coding: utf-8 -*-
from django import forms
from cmskit.articles.models import Index, Article

from cms.plugin_pool import plugin_pool
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor
from cms.plugins.text.settings import USE_TINYMCE

def get_editor_widget():
    """
    Returns the Django form Widget to be used for
    the text area
    """
    #plugins = plugin_pool.get_text_enabled_plugins(self.placeholder, self.page)        
    if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
        from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
        return TinyMCEEditor()
    else:
        return WYMEditor()

class IndexForm(forms.ModelForm):
    class Meta:
        model = Index
     
    def __init__(self, *args, **kwargs):
        super(IndexForm, self).__init__(*args, **kwargs)
        choices = [self.fields['page'].choices.__iter__().next()]
        for page in self.fields['page'].queryset:
            choices.append(
                (page.id, ''.join(['- '*page.level, page.__unicode__()]))
            )
        self.fields['page'].choices = choices
        
        
class ArticleForm(forms.ModelForm):
    
    body = forms.CharField(widget=get_editor_widget())
    
    class Meta:
        model = Article

