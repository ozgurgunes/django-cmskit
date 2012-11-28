# -*- coding: utf-8 -*-
import re
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from mptt.models import MPTTModel, TreeForeignKey
from cms.models.fields import PlaceholderField
from cms.models import CMSPlugin

from cmskit.products.managers import ProductManager


def get_upload_to(instance, filename):
    return '%s/%s/%s' % (
                str(instance._meta.app_label), 
                str(instance._meta.module_name), 
                re.sub('[^\.0-9a-zA-Z()_-]', '_', filename))


class Category(MPTTModel):

    parent          = TreeForeignKey('self', related_name='children', 
                            null=True, blank=True)
                    
    title           = models.CharField(max_length=216)
    slug            = models.SlugField(max_length=216, blank=True, null=False)
    body            = models.TextField(blank=True, null=True)
                    
    picture         = models.ImageField(_('Picture'), 
                            upload_to=get_upload_to, 
                            width_field='picture_width',
                            height_field='picture_height', 
                            blank=True, null=True)
    picture_width   = models.PositiveSmallIntegerField(_("Picture width"), 
                            editable=False, null=True)
    picture_height  = models.PositiveSmallIntegerField(_("Picture height"), 
                            editable=False, null=True)
                        
    top             = PlaceholderField('top', related_name='products_category_top')
    bottom          = PlaceholderField('bottom', related_name='products_category_bottom')
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ("tree_id", "lft")

    def __unicode__(self):
        return u"%s" % self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        url = "%s" % self.slug
        page = self
        while page.parent:
            url = "%s/%s" % (page.parent.slug,url)
            page = page.parent
        return ('products_detail', None, {'path': url})
    

class Product(models.Model):

    category        = models.ForeignKey(Category)
                    
    title           = models.CharField(_('Title'), max_length=216)
    slug            = models.SlugField(_('Slug'), max_length=216, blank=True, null=False)
    body            = models.TextField(_('Body'), blank=True, null=True)
                    
    picture         = models.ImageField(_('Picture'), 
                            upload_to=get_upload_to, 
                            width_field='picture_width',
                            height_field='picture_height', 
                            blank=True, null=True)
    picture_width   = models.PositiveSmallIntegerField(_("Picture width"), 
                            editable=False, null=True)
    picture_height  = models.PositiveSmallIntegerField(_("Picture height"), 
                            editable=False, null=True)
                    
    publish         = models.BooleanField(_('Publish'), default=True)
                    
    date_created    = models.DateTimeField(_('Creation Date'), auto_now_add=True)
    date_updated    = models.DateTimeField(_('Update Date'), auto_now=True, 
                            editable=False, blank=True, null=True)
                    
    protein         = models.DecimalField(_('Protein') + ' (%)', 
                            max_digits=5, decimal_places=2, 
                            blank=True, null=True)                      
    total_fat       = models.DecimalField(_('Total Fat') + ' (%)', 
                            max_digits=5, decimal_places=2,
                            blank=True, null=True)                      
    saturated_fat   = models.DecimalField(_('Saturated Fat') + ' (%)', 
                            max_digits=5, decimal_places=2,     
                            blank=True, null=True)                      
    energy          = models.DecimalField(_('Energy') + ' kcal/10', 
                            max_digits=5, decimal_places=2, 
                            blank=True, null=True)
                    
    cooking         = models.TextField(_('Cooking Suggestion'), blank=True, null=True)
    storage         = models.TextField(_('Storage Conditions'), blank=True, null=True)
    tricks          = models.TextField(_('Tricks'), blank=True, null=True)
    notes           = models.TextField(_('Notes'), blank=True, null=True)
                    
    top             = PlaceholderField('top', related_name='products_product_top')
    bottom          = PlaceholderField('bottom', related_name='products_product_bottom')
    
    objects         = ProductManager()
    
    class Meta:
        ordering                = ('category', 'id')
        verbose_name            = _('Product')
        verbose_name_plural     = _('Products')
        get_latest_by           = 'date_created'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return u"%s" % self.title

    @models.permalink
    def get_absolute_url(self, lang=None):
        url = "%s/%s" % (self.category.slug, self.slug)
        page = self.category
        while page.parent:
           url = "%s/%s" % (page.parent.slug, url)
           page = page.parent
        return ('products_detail', None, {'path': url}) if not lang else \
                    (lang+':products_detail', None, {'path': url})


class Info(models.Model):
    product             = models.ForeignKey(Product)
    
    title               = models.CharField(_('Title'), max_length=216)
                    
    weight              = models.PositiveIntegerField(_('Weight'), 
                                blank=True, null=True, help_text=_('grams'))
    package_quantity    = models.PositiveIntegerField(_('Package Quantity'), 
                                blank=True, null=True)
    barcode             = models.IntegerField(_('Barcode'), 
                                blank=True, null=True)
    shelf_life          = models.PositiveIntegerField(_('Shelf Life'), 
                                blank=True, null=True, help_text=_('days'))
    parcel_quantity     = models.PositiveIntegerField(_('Parcel Quantity'), 
                                blank=True, null=True)
    parcel_weight       = models.PositiveIntegerField(_('Parcel Weight'), 
                                blank=True, null=True, help_text=_('Kilograms'))
    parcel_size         = models.CharField(_('Parcel Size'), max_length=216, 
                                blank=True, null=True, help_text=_('mm'))
    
    class Meta:
        verbose_name            = _('Product information')
        verbose_name_plural     = _('Product informations')


class ProductTeaserPlugin(CMSPlugin):

    product     = models.ForeignKey(Product, blank=True, null=True)
    category    = models.ForeignKey(Category, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.product or self.category or _('All products'))

    def copy_relations(self, oldinstance):
        self.product    = oldinstance.product
        self.category   = oldinstance.category
                