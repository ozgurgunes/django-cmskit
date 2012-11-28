# -*- coding: utf-8 -*-
import re
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from cms.models import CMSPlugin, Page
from cms.models.fields import PlaceholderField

from cmskit.articles.managers import ArticleManager

def get_upload_to(instance, filename):
    return '%s/%s/%s' % (
                str(instance._meta.app_label), 
                str(instance._meta.module_name), 
                re.sub('[^\.0-9a-zA-Z()_-]', '_', filename))


class Index(models.Model):

    page        = models.ForeignKey(Page)    
    title       = models.CharField(max_length=216, blank=True)

    class Meta:
        verbose_name        = _('Index')
        verbose_name_plural = _('Indexes')
        ordering = ("title",)

    def __unicode__(self):
        return u"%s" % self.title
        
    def save(self, *args, **kwargs):
        if not self.id and not self.title:
            self.title = self.page
        super(Index, self).save(*args, **kwargs)

class Author(models.Model):
    name            = models.CharField(max_length=216)
    slug            = models.SlugField(max_length=216, blank=True, null=False)
    body            = models.TextField(blank=False, null=False)
    picture         = models.ImageField(_('Picture'), 
                            upload_to=get_upload_to, 
                            width_field='picture_width',
                            height_field='picture_height', 
                            blank=True, null=True)

    picture_width   = models.PositiveSmallIntegerField(_("Picture width"), 
                        editable=False, null=True)
    picture_height  = models.PositiveSmallIntegerField(_("Picture height"), 
                        editable=False, null=True)

    aside           = PlaceholderField('aside', related_name='articles_author_aside')    

    top             = PlaceholderField('top', related_name='articles_author_top')
    bottom          = PlaceholderField('bottom', related_name='articles_author_bottom')
                                              
    class Meta:
        verbose_name        = _('Author')
        verbose_name_plural = _('Authors')
        ordering = ("name",)

    def __unicode__(self):
        return u"%s" % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('articles_author', None, {'slug': self.slug })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)


class Article(models.Model):
    index           = models.ForeignKey(Index, blank=True, null=True)

    title           = models.CharField(_('Title'), max_length=216)
    slug            = models.SlugField(_('Slug'), max_length=216, blank=True, null=False)
    excerpt         = models.TextField(_('Excerpt'), blank=True, null=True)
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

    publish         = models.BooleanField(_('Publish'), default=False)

    date_created    = models.DateTimeField(_('Creation Date'), auto_now_add=True)
    date_updated    = models.DateTimeField(_('Update Date'), auto_now=True, 
                            editable=False, blank=True, null=True)
    date_published  = models.DateTimeField(_('Publish Date'), blank=True, null=True)

    meta            = PlaceholderField('meta', related_name='articles_article_meta')
    media           = PlaceholderField('media', related_name='articles_article_media')    
    aside           = PlaceholderField('aside', related_name='articles_article_aside')    
                      
    top             = PlaceholderField('top', related_name='articles_article_top')
    bottom          = PlaceholderField('bottom', related_name='articles_article_bottom')
    
    objects         = ArticleManager()
    
    class Meta:
        ordering                = ('-date_created', 'title')
        verbose_name            = _('Article')
        verbose_name_plural     = _('Articles')
        get_latest_by           = 'date_created'

    def __unicode__(self):
        return u"%s" % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('articles_article', None, {'slug': self.slug, 'pk': self.pk })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.publish and not self.date_published:
            self.date_published = datetime.now()
        super(Article, self).save(*args, **kwargs)


class ArticleIndex(CMSPlugin):
    index           = models.ForeignKey(Index)

    def copy_relations(self, oldinstance):
        self.index = oldinstance.index
    
    def __unicode__(self):
        return u'%s' % self.index.title


class ArticleTeaser(CMSPlugin):
    CHOICES = (
        ('random', _('Random')),
        ('latest', _('Latest'))
    )
    article     = models.ForeignKey(Article, blank=True, null=True, 
                        help_text=_('Which article will be displayed.'))
    index       = models.ForeignKey(Index, blank=True, null=True, 
                        help_text=_('Or, from which index will be displayed.'))
    select      = models.CharField(max_length=9, choices=CHOICES, blank=True, null=True, 
                        help_text=_('How the article will be chosen.'))

    def copy_relations(self, oldinstance):
        self.sections = oldinstance.sections.all()
        