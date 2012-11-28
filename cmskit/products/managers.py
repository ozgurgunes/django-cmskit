# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models


class ProductQuerySet(models.query.QuerySet):

    def published(self):
        return self.filter(publish=True)

    def translation(self, lang):
        return eval('self.exclude(slug_'+lang+'=None)')


class ProductManager(models.Manager):
    
    def get_query_set(self):
            return ProductQuerySet(self.model, using=self._db)    

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)

  
