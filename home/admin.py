from django.contrib import admin
from home.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', )
  prepopulated_fields = {
     'slug': ('name', )
  }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('p_id','p_name', 'price', 'category', 'stock') 
  prepopulated_fields = {
    "slug": ("p_name", )
  }
