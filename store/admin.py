from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    
    list_display = ("product_name", "category", "product_slug", "product_slug_uuid", "price", "stock", "images", "modified_date", "is_available",)


admin.site.register(Product, ProductAdmin)