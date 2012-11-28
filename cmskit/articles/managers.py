# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models

class ArticleQuerySet(models.query.QuerySet):

    def published(self):
        return self.filter(publish=True, date_published__lte=datetime.now())


class ArticleManager(models.Manager):

    def get_query_set(self):
            return ArticleQuerySet(self.model, using=self._db)    

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)


