from django.contrib import admin

from parser.models import Product


class ApiAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']


admin.site.register(Product, ApiAdmin)