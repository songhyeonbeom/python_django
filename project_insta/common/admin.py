from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display_links = ['id', 'username', ]
    list_display = ('id', 'username', 'email', 'gender2', 'is_admin')
    list_filter = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',
                           'realname', 'birth_date', 'phone', 'gender', 'gender2')}),

        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'realname', 'birth_date', 'phone', 'gender', 'gender2'
                       , 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email', 'gender2', )
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)