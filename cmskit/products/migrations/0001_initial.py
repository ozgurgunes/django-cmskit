# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('products_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['products.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=216)),
            ('title_tr', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('title_ar', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=216, blank=True)),
            ('slug_tr', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=216, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=216, null=True, blank=True)),
            ('slug_ar', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=216, null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body_tr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('picture_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('picture_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('top', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products_category_top', null=True, to=orm['cms.Placeholder'])),
            ('bottom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products_category_bottom', null=True, to=orm['cms.Placeholder'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('products', ['Category'])

        # Adding model 'Product'
        db.create_table('products_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=216)),
            ('title_tr', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('title_ar', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=216, blank=True)),
            ('slug_tr', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=216, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=216, null=True, blank=True)),
            ('slug_ar', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=216, null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body_tr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('picture_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('picture_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('protein', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('total_fat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('saturated_fat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('energy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('cooking', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cooking_tr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cooking_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cooking_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('storage', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('storage_tr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('storage_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('storage_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tricks', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tricks_tr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tricks_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tricks_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes_tr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('top', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products_product_top', null=True, to=orm['cms.Placeholder'])),
            ('bottom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products_product_bottom', null=True, to=orm['cms.Placeholder'])),
        ))
        db.send_create_signal('products', ['Product'])

        # Adding model 'Info'
        db.create_table('products_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=216)),
            ('title_tr', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('title_ar', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('package_quantity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('barcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('shelf_life', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('parcel_quantity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('parcel_weight', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('parcel_size', self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True)),
        ))
        db.send_create_signal('products', ['Info'])

        # Adding model 'ProductTeaserPlugin'
        db.create_table('cmsplugin_productteaserplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'], null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('products', ['ProductTeaserPlugin'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('products_category')

        # Deleting model 'Product'
        db.delete_table('products_product')

        # Deleting model 'Info'
        db.delete_table('products_info')

        # Deleting model 'ProductTeaserPlugin'
        db.delete_table('cmsplugin_productteaserplugin')


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
        'products.info': {
            'Meta': {'object_name': 'Info'},
            'barcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package_quantity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parcel_quantity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parcel_size': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'parcel_weight': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'shelf_life': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '216'}),
            'title_ar': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'title_tr': ('django.db.models.fields.CharField', [], {'max_length': '216', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
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
        'products.productteaserplugin': {
            'Meta': {'object_name': 'ProductTeaserPlugin', 'db_table': "'cmsplugin_productteaserplugin'", '_ormbases': ['cms.CMSPlugin']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']", 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['products']