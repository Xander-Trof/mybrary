from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from book_auth_app.models import CustomUser
# Register your models here.


class CustomAdminModel(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Other', {'fields': (
            'our_note',
        )}),
    )
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
    )
    list_editable = ()
    list_filter = (
    )
    search_fields = (
        'first_name',
        'last_name',
        'username',
    )


admin.site.register(CustomUser, CustomAdminModel)
