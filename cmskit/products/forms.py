# -*- coding: utf-8 -*-
from django import forms
from mptt.forms import TreeNodeChoiceField
from cmskit.products.models import Product, Category

class ProductForm(forms.ModelForm):
    category = TreeNodeChoiceField(Category.objects.all())
    
    class Meta:
        model = Product
        #fields = ('protein',)

