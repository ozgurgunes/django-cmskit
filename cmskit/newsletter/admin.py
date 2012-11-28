from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.defaults import *

from cmskit.newsletter.models import Subscription
from cmskit.newsletter.forms import SubscriptionForm
from cmskit.newsletter.views import export_csv

class SubscriptionAdmin(admin.ModelAdmin):
    
    list_display = ('email', 'subscribed', 'created_on', )
    search_fields = ('email',)
    list_filter = ('subscribed',)
    actions = ['mark_subscribed', 'mark_unsubscribed']
    
    # define custom views for the admin
    def export_csv_view(self, request):
        return export_csv(request, self.model)

    # hook custom views into admin site urls
    def get_urls(self):
        urls = super(SubscriptionAdmin, self).get_urls()
        csv_urls = patterns('',
            url(r'^export-csv/$',
                view=self.export_csv_view,
                name='export_csv',
            ),
        )
        return csv_urls + urls
            
    # action definitions
    def mark_subscribed(self, request, queryset):
        rows_updated = queryset.update(subscribed=True)
        mpart1 = (_('One email was') if rows_updated == 1 else _('%s emails were') % rows_updated)
        message = mpart1 + _(' successfully marked as subscribed.')
        self.message_user(request, message)
    mark_subscribed.short_description = _('Mark as subscribed')

    def mark_unsubscribed(self, request, queryset):
        rows_updated = queryset.update(subscribed=False)
        mpart1 = (_('One email was') if rows_updated == 1 else _('%s emails were') % rows_updated)
        message = mpart1 + _(' successfully marked as unsubscribed.')
        self.message_user(request, message)
    mark_unsubscribed.short_description = _('Mark as unsubscribed')    
    
admin.site.register(Subscription, SubscriptionAdmin)