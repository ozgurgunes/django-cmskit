from django.conf import settings
from django.contrib.admin import TabularInline, StackedInline

JS = (
    # settings.STATIC_URL + 'js/jquery-1.8.2.min.js',
    # settings.STATIC_URL + 'js/jquery-ui-1.8.24.custom.min.js',
    # settings.STATIC_URL + 'js/ordering.js',
)

class OrderableStackedInline(StackedInline):
    
    """Adds necessary media files to regular Django StackedInline"""
    
    class Media:
        js  = JS


class OrderableTabularInline(TabularInline):
    
    """Adds necessary media files to regular Django TabularInline"""
    
    class Media:
        js = JS
