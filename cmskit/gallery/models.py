# -*- coding: utf-8 -*-
import re

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page

from cmskit.utils.models import Orderable


def get_upload_to(instance, filename):
    return '%s/%s/%s' % (
                str(instance._meta.app_label), 
                str(instance._meta.module_name), 
                re.sub('[^\.0-9a-zA-Z()_-]', '_', filename))


class Gallery(models.Model):
    
    page        = models.ForeignKey(Page)    
    title       = models.CharField(_('Title'), max_length=216, blank=True)

    class Meta:
        verbose_name        = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __unicode__(self):
        return _(u'%s (%s)') % (self.title, self.image_set.count())

    def save(self, *args, **kwargs):
        if not self.id and not self.title:
            self.title = self.page
        super(Gallery, self).save(*args, **kwargs)

class Image(Orderable):

    gallery     = models.ForeignKey(Gallery)
    
    src         = models.ImageField(_("Image file"), 
                        upload_to=get_upload_to,
                        width_field='src_width',
                        height_field='src_height') 
                            
    src_width   = models.PositiveSmallIntegerField(_("Image width"), 
                        editable=False, null=True)
    src_height  = models.PositiveSmallIntegerField(_("Image height"), 
                        editable=False, null=True)
                            
    title       = models.CharField(_("Title"), max_length=255, blank=True, null=True)
    alt         = models.TextField(_("Alt text"), blank=True, null=True)

    class Meta(Orderable.Meta):
        verbose_name        = _('Image')
        verbose_name_plural = _('Images')

    def __unicode__(self):
        return self.title or self.alt or str(self.pk)
        
        
class ImageGallery(CMSPlugin):
    
    gallery         = models.ForeignKey(Gallery)

    def __unicode__(self):
        return u'%s' % self.gallery.title

    def copy_relations(self, oldinstance):
        self.gallery = oldinstance.gallery
