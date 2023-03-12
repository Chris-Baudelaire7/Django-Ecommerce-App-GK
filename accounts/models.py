from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccountManager(BaseUserManager):
    
    def create_user(self, first_name, last_name, username, email, password=None):
    
        if not email:
            raise ValueError("Vous devez obligatoirement renseigné une adresse email")
        
        if not username:
            raise ValueError("Vous devez obligatoirement renseigné un nom d'utilisateur")
        
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
            username = username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    
    def create_superuser(self, first_name, last_name, username, email, password):
        
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email),
            password = password,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class Account(AbstractBaseUser):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    
    objects = MyAccountManager()
    
    
    def has_perm(self, perm, obj=None):
        
        return self.is_admin
    
    
    def has_module_perms(self, add_label):
        
        return True
    
    
    def __str__(self):
        
        return self.email