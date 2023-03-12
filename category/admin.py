from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ("category_name", "description", "category_slug", "category_slug_uuid", "cat_image",)


admin.site.register(Category, CategoryAdmin)