from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_date')
    search_fields = ('category_name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'availability')
    search_fields = ('product_name', 'description')
    list_filter = ('category',)

# Register the models with their admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)