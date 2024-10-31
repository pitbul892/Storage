from django.contrib import admin

from .models import Product, Type


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'barcode')


admin.site.register(Product, ProductAdmin)
admin.site.register(Type)
