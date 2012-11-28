# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Info.title_en'
        db.delete_column('products_info', 'title_en')

        # Deleting field 'Info.title_ar'
        db.delete_column('products_info', 'title_ar')

        # Deleting field 'Info.title_tr'
        db.delete_column('products_info', 'title_tr')


    def backwards(self, orm):
        # Adding field 'Info.title_en'
        db.add_column('products_info', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Info.title_ar'
        db.add_column('products_info', 'title_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Info.title_tr'
        db.add_column('products_info', 'title_tr',
                      self.gf('django.db.models.fields.CharField')(max_length=216, null=True, blank=True),
                      keep_default=False)


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