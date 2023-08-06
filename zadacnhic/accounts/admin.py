from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

from accounts.forms import AdminUserChangeForm, SignUpForm
from accounts.models import Profile, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'get_profile_link',
        'get_profile_admin_link',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    readonly_fields = (
        'id',
        'date_joined',
        'last_login',
    )
    ordering = ('email',)

    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )

    form = AdminUserChangeForm
    fieldsets = (
        (None, {'fields': ('email',)}),
        (
            'Personal info', {
                'fields': ('first_name', 'last_name'),
            },
        ),
        (
            'Permissions', {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )

    add_form = SignUpForm
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide', ),
                'fields': (
                    'email',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                ),
            },
        ),
    )

    def get_profile_link(self, obj: User):
        return mark_safe(
            f"""<a href="{reverse('profile_view', args=(obj.id, ))}">Просмотреть</a>""",
        )

    get_profile_link.short_description = 'Профиль на сайте'

    def get_profile_admin_link(self, obj: User):
        return mark_safe(
            f"""<a href="{
                reverse('admin:accounts_profile_change', args=(obj.id, ))
            }">Просмотреть</a>""",
        )

    get_profile_admin_link.short_description = 'Ссылка на профиль в панели администратора'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'date_of_birth',
        'gender',
        'get_profile_link',
        'get_user_admin_link',
    )
    search_fields = ('user__email', )

    def get_profile_link(self, obj: User):
        return mark_safe(
            f"""<a href="{reverse('profile_view', args=(obj.id, ))}">Просмотреть</a>""",
        )

    get_profile_link.short_description = 'Профиль на сайте'

    def get_user_admin_link(self, obj: User):
        return mark_safe(
            f"""<a href="{
                reverse('admin:accounts_user_change', args=(obj.id, ))
            }">Просмотреть</a>""",
        )

    get_user_admin_link.short_description = 'Ссылка на пользователя в панели администратора'
