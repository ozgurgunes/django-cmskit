# -*- coding: utf-8 -*-
import re
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries import CountryField


def get_upload_to(instance, filename):
    return '%s/%s/%s' % (
                str(instance._meta.app_label), 
                str(instance._meta.module_name), 
                re.sub('[^\.0-9a-zA-Z()_-]', '_', filename))


class DealerQuerySet(models.query.QuerySet):

    def published(self):
        return self.filter(publish=True)


class DealerManager(models.Manager):

    def get_query_set(self):
            return DealerQuerySet(self.model, using=self._db)    

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)


class Dealer(models.Model):

    title           = models.CharField(_(u'Title'), max_length=255)
    description     = models.TextField(_(u'Description'), blank=True, null=True)
    picture         = models.ImageField(_('Picture'), 
                            upload_to=get_upload_to, 
                            width_field='picture_width',
                            height_field='picture_height', 
                            blank=True, null=True)
    picture_width   = models.PositiveSmallIntegerField(_("Picture width"), 
                            editable=False, null=True)
    picture_height  = models.PositiveSmallIntegerField(_("Picture height"), 
                            editable=False, null=True)                      
                      

    phone           = models.CharField(_(u'Phone number'), max_length=24, 
                            blank=True, null=True)
    fax             = models.CharField(_(u'Fax number'), max_length=24, 
                            blank=True, null=True)
                    
    street          = models.TextField(_(u'Street'), max_length=255, 
                            blank=True, null=True)
    zipcode         = models.CharField(_(u'Zip code'), max_length=8, 
                            blank=True, null=True)
    city            = models.CharField(_(u'City'), max_length=64, 
                            blank=True, null=True)
    country         = CountryField(_(u'Country'), blank=True, null=True)
                    
    website         = models.URLField(_(u'Website'), max_length=255, 
                            blank=True, null=True)
                    
    latitude        = models.FloatField(_(u'Latitude'), blank=True, null=True)
    longitude       = models.FloatField(_(u'Longitude'), blank=True, null=True)

    publish         = models.BooleanField(_('Publish'), default=False)

    date_created    = models.DateTimeField(_('Creation Date'), auto_now_add=True)
    date_updated    = models.DateTimeField(_('Update Date'), auto_now=True, 
                            editable=False, blank=True, null=True)

    objects         = DealerManager()
    
    class Meta:
        verbose_name        = _('Dealer')
        verbose_name_plural = _('Dealers')

    def __unicode__(self):
        return self.title
        
    def coordinates(self):
        return u'%s, %s' % (self.latitude, self.longitude)
    