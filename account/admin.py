from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from account.forms import AppealCreateForm
from account.models import CustomUser, Profile, Appeal


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('surname', 'room_number', 'phone', 'university', 'hostel')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):

    list_display = ('email', 'ip_address', 'user', 'time_create')
    list_display_links = ('email', 'ip_address')

