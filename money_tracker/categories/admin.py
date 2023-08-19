from django.contrib import admin

from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'slug',
    )
    search_fields = (
        'user',
        'name',
    )
    prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('id', )
    ordering = ('user',)
    list_filter = ('user', )
