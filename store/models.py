from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from category.models import Category
import uuid


class Product(models.Model):
    
    product_name = models.CharField(max_length=255, unique=True)
    product_slug = models.SlugField(max_length=255, blank=True, unique=True)
    product_slug_uuid = models.SlugField(max_length=255, blank=True, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to="photos/products", blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    class Meta:
        
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
        
    def __str__(self):
        
        return self.product_name
        
    
    def save(self, *args, **kwargs):
        
        if not self.product_slug_uuid:
            self.product_slug_uuid = slugify(self.product_name) + "-" + str(uuid.uuid4())
            
        if not self.product_slug:
            self.product_slug = slugify(self.product_name)
            
        return super().save(*args, **kwargs)
    
    
    def get_url(self):
      
        return reverse("product_detail", kwargs={
            "category_slug": self.category.category_slug,
            "product_slug": self.product_slug
        })
    
    
    