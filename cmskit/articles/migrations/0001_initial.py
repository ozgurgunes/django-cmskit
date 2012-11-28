# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Index'
        db.create_table('articles_index', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Page'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=216, blank=True)),
        ))
        db.send_create_signal('articles', ['Index'])

        # Adding model 'Author'
        db.create_table('articles_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=216)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=216, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('picture_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('picture_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('aside', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_author_aside', null=True, to=orm['cms.Placeholder'])),
            ('top', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_author_top', null=True, to=orm['cms.Placeholder'])),
            ('bottom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_author_bottom', null=True, to=orm['cms.Placeholder'])),
        ))
        db.send_create_signal('articles', ['Author'])

        # Adding model 'Article'
        db.create_table('articles_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('index', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Index'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=216)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=216, blank=True)),
            ('excerpt', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('picture_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('picture_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('meta', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_article_meta', null=True, to=orm['cms.Placeholder'])),
            ('media', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_article_media', null=True, to=orm['cms.Placeholder'])),
            ('aside', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_article_aside', null=True, to=orm['cms.Placeholder'])),
            ('top', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_article_top', null=True, to=orm['cms.Placeholder'])),
            ('bottom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_article_bottom', null=True, to=orm['cms.Placeholder'])),
        ))
        db.send_create_signal('articles', ['Article'])

        # Adding model 'ArticleIndex'
        db.create_table('cmsplugin_articleindex', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('index', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Index'])),
        ))
        db.send_create_signal('articles', ['ArticleIndex'])

        # Adding model 'ArticleTeaser'
        db.create_table('cmsplugin_articleteaser', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Article'], null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Index'], null=True, blank=True)),
            ('select', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
        ))
        db.send_create_signal('articles', ['ArticleTeaser'])


    def backwards(self, orm):
        # Deleting model 'Index'
        db.delete_table('articles_index')

        # Deleting model 'Author'
        db.delete_table('articles_author')

        # Deleting model 'Article'
        db.delete_table('articles_article')

        # Deleting model 'ArticleIndex'
        db.delete_table('cmsplugin_articleindex')

        # Deleting model 'ArticleTeaser'
        db.delete_table('cmsplugin_articleteaser')


    models = {
        'articles.article': {
            'Meta': {'ordering': "('-date_created', 'title')", 'object_name': 'Article'},
            'aside': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_article_aside'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bottom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_article_bottom'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articles.Index']", 'null': 'True', 'blank': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_article_media'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_article_meta'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'picture_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '216', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '216'}),
            'top': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_article_top'", 'null': 'True', 'to': "orm['cms.Placeholder']"})
        },
        'articles.articleindex': {
            'Meta': {'object_name': 'ArticleIndex', 'db_table': "'cmsplugin_articleindex'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'index': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articles.Index']"})
        },
        'articles.articleteaser': {
            'Meta': {'object_name': 'ArticleTeaser', 'db_table': "'cmsplugin_articleteaser'", '_ormbases': ['cms.CMSPlugin']},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articles.Article']", 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'index': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articles.Index']", 'null': 'True', 'blank': 'True'}),
            'select': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        'articles.author': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Author'},
            'aside': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_author_aside'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'bottom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_author_bottom'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '216'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'picture_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '216', 'blank': 'True'}),
            'top': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_author_top'", 'null': 'True', 'to': "orm['cms.Placeholder']"})
        },
        'articles.index': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Index'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '216', 'blank': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'Meta': {'ordering': "('site', 'tree_id', 'lft')", 'object_name': 'Page'},
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderator_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['articles']