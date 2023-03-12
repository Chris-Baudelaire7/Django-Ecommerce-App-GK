from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid


class Category(models.Model):
    
    category_name = models.CharField(max_length=255, unique=True)
    category_slug = models.SlugField(max_length=255, unique=True, blank=True)
    category_slug_uuid = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to="photos/categories", blank=True)
    
    
    class Meta:
        
        verbose_name = "Category"
        verbose_name_plural = "categories"
        
        
    def __str__(self):
        
        return self.category_name
    
    
    def save(self, *args, **kwargs):
        
        if not self.category_slug_uuid:
            self.category_slug_uuid = slugify(self.category_name) + "-" + str(uuid.uuid4())
            
        if not self.category_slug:
            self.category_slug = slugify(self.category_name)
            
        return super().save(*args, **kwargs)
    
    
    def get_url(self):
        
        return reverse("products_by_category", kwargs={"category_slug": self.category_slug})
    
    
    