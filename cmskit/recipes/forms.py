# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from models import Recipe

class RecipeForm(forms.ModelForm):
    token           = forms.CharField()
    title           = forms.CharField()
    ingredients     = forms.CharField(widget=forms.Textarea())
    directions      = forms.CharField(widget=forms.Textarea())
    picture         = forms.ImageField()
    
    class Meta:
        model       = Recipe
        fields      = ['token', 'title', 'ingredients', 'directions', 'picture']
    
    def clean_token(self):
        token = getattr(settings, 'RECIPE_API_TOKEN', None)
        if not self.cleaned_data.get('token') == token:
            raise forms.ValidationError(_(u'Invalid token.'))
        return self.cleaned_data['token']
        
    def clean_picture(self):
        """
        Validates format and file size of uploaded picture.
        
        """
        formats = getattr(settings, 'RECIPE_PICTURE_FORMATS', ['jpeg', 'gif', 'png'])
        max_file = getattr(settings, 'RECIPE_PICTURE_MAX_FILE', 1024*1024)
        
        if self.cleaned_data.get('picture'):
            picture_data = self.cleaned_data['picture']
            if 'error' in picture_data:
                raise forms.ValidationError(_(u'Upload a valid image. '
                            'The file you uploaded was either not an image '
                            'or a corrupted image.'))
                
            content_type = picture_data.content_type
            if content_type:
                main, sub = content_type.split('/')
                if not (main == 'image' and sub in formats):
                    raise forms.ValidationError(_(u'%s only.' % formats))
        
            if picture_data.size > int(max_file):
                raise forms.ValidationError(_(u'Image size is too big.'))
            return self.cleaned_data['picture']
