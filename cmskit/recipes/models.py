# -*- coding: utf-8 -*-
import re
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField

from tagging.models import Tag
from tagging.fields import TagField

from cmskit.products.models import Product


def get_upload_to(instance, filename):
    return '%s/%s/%s' % (
                str(instance._meta.app_label), 
                str(instance._meta.module_name), 
                re.sub('[^\.0-9a-zA-Z()_-]', '_', filename))


class RecipeQuerySet(models.query.QuerySet):

    def published(self):
        return self.filter(publish=True)


class RecipeManager(models.Manager):

    def get_query_set(self):
            return RecipeQuerySet(self.model, using=self._db)    

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)


class Recipe(models.Model):
    products            = models.ManyToManyField(Product, blank=True, null=True)
                      
    title               = models.CharField(_('Title'), max_length=216)
    slug                = models.SlugField(_('Slug'), max_length=216, blank=True, null=False)

    picture             = models.ImageField(_('Picture'), 
                                upload_to=get_upload_to, 
                                width_field='picture_width',
                                height_field='picture_height', 
                                blank=True, null=True)
    picture_width       = models.PositiveSmallIntegerField(_("Picture width"), 
                                editable=False, null=True)
    picture_height      = models.PositiveSmallIntegerField(_("Picture height"), 
                                editable=False, null=True)                      
                      
    ingredients         = models.TextField(_('Ingredients'), blank=True, null=True)
    directions          = models.TextField(_('Directions'), blank=True, null=True)

    preperation_time    = models.PositiveIntegerField(_('Preperation Time'), 
                                blank=True, null=True, help_text=_('minutes'))
    cooking_time        = models.PositiveIntegerField(_('Cooking Time'), 
                                blank=True, null=True, help_text=_('minutes'))
    
    publish             = models.BooleanField(_('Publish'), default=False)
                        
    date_created        = models.DateTimeField(_('Creation Date'), auto_now_add=True)
    date_updated        = models.DateTimeField(_('Update Date'), auto_now=True, 
                                editable=False, blank=True, null=True)

    tags                = TagField()

    aside               = PlaceholderField('aside', related_name='recipes_recipe_aside')
    top                 = PlaceholderField('top', related_name='recipes_recipe_top')
    bottom              = PlaceholderField('bottom', related_name='recipes_recipe_bottom')
    
    objects             = RecipeManager()
    
    class Meta:
        ordering                = ('title',)
        verbose_name            = _('Recipe')
        verbose_name_plural     = _('Recipes')

    def __unicode__(self):
        return u"%s" % self.title
        
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Recipe, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('recipes_recipe', None, {'slug': self.slug })

    def total_time(self):
        return self.preperation_time + self.cooking_time

    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    def _set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    tag_list = property(_get_tags, _set_tags)


class RecipeTeaserPlugin(CMSPlugin):
    recipe = models.ForeignKey(Recipe, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.recipe.title

    def copy_relations(self, oldinstance):
        self.recipe = oldinstance.recipe
        

