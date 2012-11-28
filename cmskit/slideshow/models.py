# -*- coding: utf-8 -*-
import re
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from cmskit.utils.models import Orderable


def get_upload_to(instance, filename):
    return '%s/%s/%s' % (
                str(instance._meta.app_label), 
                str(instance._meta.module_name), 
                re.sub('[^\.0-9a-zA-Z()_-]', '_', filename))


class Slideshow(CMSPlugin):

    def __unicode__(self):
        return _(u'%(count)d slide(s)') % {'count': self.slide_set.count()}
        
    def copy_relations(self, oldinstance):
        self.slide_set = oldinstance.slide_set.all()
    

class SlideQuerySet(models.query.QuerySet):

    def published(self):
        return self.filter(publish=True)


class SlideManager(models.Manager):

    def get_query_set(self):
            return SlideQuerySet(self.model, using=self._db)    

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)


class Slide(Orderable):
    
    slideshow       = models.ForeignKey(Slideshow, verbose_name=_('Slideshow'))
    
    title           = models.CharField(_('Title'), max_length=216, blank=True, null=True, 
                            help_text=_('A descriptive title for the slide'))
    summary         = models.TextField(_('Summary'), blank=True, null=True, 
                            help_text=_('A descriptive summary for the slide'))
    picture         = models.ImageField(_('Picture'), 
                            upload_to=get_upload_to, 
                            width_field='picture_width',
                            height_field='picture_height', 
                            blank=True, null=True,
                            help_text=_('Please upload a JPG or PNG image'))
    picture_width   = models.PositiveSmallIntegerField(_("Picture width"), 
                            editable=False, null=True)
    picture_height  = models.PositiveSmallIntegerField(_("Picture height"), 
                            editable=False, null=True)                      

    alt             = models.TextField(_("Alt text"), blank=True, null=True)
    url             = models.CharField(_('URL'), max_length=216,
                            help_text=_('Target link for the slide'))

    publish         = models.BooleanField(_('Publish'), default=False)

    date_created    = models.DateTimeField(_('Creation Date'), auto_now_add=True)
    date_updated    = models.DateTimeField(_('Update Date'), auto_now=True, 
                            editable=False, blank=True, null=True)
                            
    objects         = SlideManager()

    class Meta(Orderable.Meta):
        verbose_name        = _('Slide')
        verbose_name_plural = _('Slides')

    def __unicode__(self):
        return u"%s" % str(self.pk)
