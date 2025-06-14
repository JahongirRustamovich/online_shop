from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # avtomatik slug

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created')
    list_filter = ('available', 'created', 'category')  # filter panel
    search_fields = ('name', 'description')             # qidiruv
    prepopulated_fields = {'slug': ('name',)}           # avtomatik slug



