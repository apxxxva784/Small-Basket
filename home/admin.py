from django.contrib import admin
from home.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('p_id','p_name', 'price', 'category', 'stock')
