from django.contrib import admin
from core.models import MyOwnToken
# Register your models here.

# admin.site.register(MyOwnToken)

class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created', 'openstack_cache', 'expired')
    fields = ('user', 'expired', 'openstack_cache')
    ordering = ('-created',)


admin.site.register(MyOwnToken, TokenAdmin)