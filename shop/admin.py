from django.contrib import admin

# Register your models here.
from .models import Product, Thumbnail, Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'quantity', 'published', 'created_at', 'updated_at']
    list_filter = ['published', 'created_at', 'updated_at']
    list_editable = ['price', 'quantity', 'published']
    prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Thumbnail)