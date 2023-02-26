from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'name', 'dateJoined', 'lastLogin', 'is_active', 'is_staff', 'is_superuser', 'is_admin')
    search_fields = ('email', 'username', 'name')

    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
