# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table('recipes_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=216)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=216, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('picture_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('picture_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('ingredients', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('directions', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('preperation_time', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('cooking_time', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('aside', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipes_recipe_aside', null=True, to=orm['cms.Placeholder'])),
            ('top', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipes_recipe_top', null=True, to=orm['cms.Placeholder'])),
            ('bottom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipes_recipe_bottom', null=True, to=orm['cms.Placeholder'])),
        ))
        db.send_create_signal('recipes', ['Recipe'])

        # Adding M2M table for field products on 'Recipe'
        db.create_table('recipes_recipe_products', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False)),
            ('product', models.ForeignKey(orm['products.product'], null=False))
        ))
        db.create_unique('recipes_recipe_products', ['recipe_id', 'product_id'])

        # Adding model 'RecipeTeaserPlugin'
        db.create_table('cmsplugin_recipeteaserplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'], null=True, blank=True)),
        ))
        db.send_create_signal('recipes', ['RecipeTeaserPlugin'])


    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')

        # Removing M2M table for field products on 'Recipe'
        db.delete_table('recipes_recipe_products')

        # Deleting model 'RecipeTeaserPlugin'
        db.delete_table('cmsplugin_recipeteaserplugin')


    models = {
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
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'products.category': {
            'Meta': {'ordering': "('tree_id', 'lft')", 'object_name': 'Category'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_tr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bottom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products_category_bottom'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['products.Category']"}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'picture_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '216', 'blank': 'True'}),
            'slug_ar': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'slug_tr': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '216'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'title_tr': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'top': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products_category_top'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'products.product': {
            'Meta': {'ordering': "('category', 'id')", 'object_name': 'Product'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_tr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bottom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products_product_bottom'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'cooking': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cooking_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cooking_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cooking_tr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'energy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes_tr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'picture_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'protein': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'saturated_fat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '216', 'blank': 'True'}),
            'slug_ar': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'slug_tr': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'storage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'storage_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'storage_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'storage_tr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '216'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'title_tr': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'top': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products_product_top'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'total_fat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'tricks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tricks_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tricks_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tricks_tr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'recipes.recipe': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Recipe'},
            'aside': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipes_recipe_aside'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'bottom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipes_recipe_bottom'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'cooking_time': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'directions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'picture_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'picture_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'preperation_time': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['products.Product']", 'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '216', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '216'}),
            'top': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipes_recipe_top'", 'null': 'True', 'to': "orm['cms.Placeholder']"})
        },
        'recipes.recipeteaserplugin': {
            'Meta': {'object_name': 'RecipeTeaserPlugin', 'db_table': "'cmsplugin_recipeteaserplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['recipes']