# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cmskit.products.models import Category, Product, Info
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline, TranslationTabularInline
from mptt.admin import MPTTModelAdmin
from cmskit.products.forms import ProductForm
from cms.admin.placeholderadmin import PlaceholderAdmin
from reversion import VersionAdmin
from treeadmin.admin import TreeAdmin

class AdminBase(TranslationAdmin):
    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            '//ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }        

class CategoryAdmin(PlaceholderAdmin, AdminBase, TreeAdmin):
    def product_count(self, instance):
        return instance.product_set.count()
        
    list_display = ('title', 'slug', 'product_count')
    fields = ('title', 'body', 'slug', 'top', 'bottom')
    # prepopulated_fields = {"slug": ("title",)}

#class InfoInline(TranslationStackedInline):
class InfoInline(admin.StackedInline):
    model = Info
    #max_num = 1
    extra = 1
    fields = ('title', ('weight', 'barcode'), ('shelf_life', 'package_quantity'), ('parcel_quantity', 'parcel_weight'), 'parcel_size')

class ProductAdmin(PlaceholderAdmin, AdminBase, VersionAdmin):
    def category_display(self, instance):
        title = page = instance.category
        while page.parent:
           title = "%s > %s" % (page.parent, title)
           page = page.parent
        return title
        
    list_display = ('title', 'slug', 'category_display', 'publish')
    save_on_top = True
    form = ProductForm
    
    fieldsets = (
            (None, {
                'fields': ('category', 'title', 'slug', 'body', 'picture',
                    'publish', ('date_created', 'date_updated'),
                    ('protein', 'total_fat', 'saturated_fat', 'energy'), 'top', 'bottom')
            }),
            (_('Extra'), {
                'classes': ('collapse',),
                'fields': ('cooking', 'storage', 'tricks', 'notes')
            }),
        )
    readonly_fields = ('date_created', 'date_updated')
    
    inlines = [InfoInline,]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
