# store/admin.py

from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # This pre-populates the slug field based on the name
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'mrp')
    list_filter = ('category', 'brand')
    search_fields = ('name', 'brand')

    fieldsets = (
        (None, {
            'fields': ('name', 'brand', 'image', 'category')
        }),
        ('Pricing', {
            'fields': ('price', 'mrp'),
        }),
    )
