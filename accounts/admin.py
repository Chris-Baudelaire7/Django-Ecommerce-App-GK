from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    
    list_display = ("first_name", "last_name", "username", "email", "phone_number", "last_login", "date_joined", "is_active",)
    
    list_display_links = ("first_name", "last_name", "username", "email",)
    
    read_only_fields = ("phone_number", "last_login", "date_joined", "is_active",)
    
    ordering = ("-date_joined",)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)