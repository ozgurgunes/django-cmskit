# -*- coding: utf-8 -*-
from django import forms
from models import Dealer
from django.contrib.localflavor.tr import forms as local_forms
from django.contrib.localflavor.tr.tr_provinces import PROVINCE_CHOICES

class DealerForm(forms.ModelForm):

    phone       = local_forms.TRPhoneNumberField(required=False)
    fax         = local_forms.TRPhoneNumberField(required=False)

    zipcode     = local_forms.TRPostalCodeField(required=False)
    city        = forms.ChoiceField(required=False, 
                    choices=list([('','')] + list(PROVINCE_CHOICES)))
    
    class Meta:
        model = Dealer


class SearchForm(forms.Form):
    keywords    = forms.CharField();
    city        = forms.ChoiceField(choices=list([('','')] + list(PROVINCE_CHOICES)))
    
