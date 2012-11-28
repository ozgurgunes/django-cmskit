from django.conf import settings
import itertools
from cms.sitemaps import CMSSitemap
from django.core.exceptions import ObjectDoesNotExist

class MultilingualCMSSitemap(CMSSitemap):
   def items(self):
       items = itertools.chain.from_iterable([(lang, item) \
                    for lang, language in settings.LANGUAGES] \
                    for item in super(MultilingualCMSSitemap, self).items())
       ret = []
       for lang, item in items:
           try:
               item.get_absolute_url(lang, False)
               ret.append((lang, item))
           except ObjectDoesNotExist:
               pass
       return ret

   def location(self, (lang, obj)):
       return '/'+lang+obj.get_absolute_url(lang, False)

   def lastmod(self, (lang, obj)):
       return super(MultilingualCMSSitemap, self).lastmod(obj)