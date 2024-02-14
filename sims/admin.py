from django.contrib import admin
from .  models import *

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username', 'password1', 'password2'),
        }),
    )

    ordering=('email',)
    

# Register your models here.
admin.site.register(MyStudents, MyUserAdmin)
admin.site.register(MyStaff, MyUserAdmin)
admin.site.register(Patient)
admin.site.register(Patientinfo)
admin.site.register(StaffContactinfo)