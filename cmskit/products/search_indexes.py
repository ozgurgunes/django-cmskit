# -*- coding: utf-8 -*-
from django.conf import settings
from haystack import site, indexes
from cmskit.products.models import Product
from cmskit.products.managers import ProductManager
from cms_search.search_helpers.indexes import MultiLanguageIndex
from django.utils.translation import activate, deactivate, get_language, string_concat, ugettext_lazy


# class ProductIndex(MultiLanguageIndex):
#     title   = indexes.CharField(model_attr='title')
#     url     = indexes.CharField(stored=True)
#     text    = indexes.CharField(document=True, use_template=True, 
#                     template_name='search/products/product_index.txt')
# 
#     def index_queryset(self):
#         """Used when the entire index for model is updated."""
#         return Product.objects.published().select_related()
#         
#     def prepare_url(self, obj):
#         try:
#             return '/%s%s' % (get_language(), obj.get_absolute_url())
#         except:
#             pass
#         
#     class HaystackTrans:
#         fields = ('url', 'title')
# 
# site.register(Product, ProductIndex)


def product_index_factory(lang, lang_name):
    if isinstance(lang_name, basestring):
        lang_name = ugettext_lazy(lang_name)

    def get_absolute_url(self):
        return '/%s%s' % (lang, Product.get_absolute_url(self))

    class Meta:
        proxy = True
        #app_label = 'products'
        verbose_name = string_concat(Product._meta.verbose_name, ' (', lang_name, ')')
        verbose_name_plural = string_concat(Product._meta.verbose_name_plural, ' (', lang_name, ')')
        
    attrs = {'__module__': Product.__module__, 
             'Meta': Meta,
             'objects': ProductManager(),
             'get_absolute_url': get_absolute_url}
    
    _ProductProxy = type("Product%s" % lang.title() , (Product,), attrs)
        
    class _ProductIndex(indexes.SearchIndex):
        
        title   = indexes.CharField(model_attr='title')
        url     = indexes.CharField(stored=True, model_attr='get_absolute_url')
        text    = indexes.CharField(document=True, use_template=True, 
                        template_name='search/products/product_index.txt')

        def index_queryset(self):
            query = _ProductProxy.objects.published().select_related()
            return eval('query.exclude(title_'+lang+'__isnull=True)')
        
        def prepare(self, obj):
            activate(lang)
            self.prepared_data = super(_ProductIndex, self).prepare(obj)
            deactivate()
            return self.prepared_data
            
    return _ProductProxy, _ProductIndex

for lang_tuple in settings.LANGUAGES:
    lang, lang_name = lang_tuple
    site.register(*product_index_factory(lang, lang_name))
    