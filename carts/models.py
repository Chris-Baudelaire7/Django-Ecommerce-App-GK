from django.db import models
from store.models import Product


class Cart(models.Model):
    
    cart_id = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        
        return self.cart_id
    
    
class CartItem(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        
        return self.product
    
    
    @property
    def sub_total(self):
        
        total = self.product.price * self.quantity
        
        return total