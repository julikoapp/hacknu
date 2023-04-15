from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class Operator(BaseUserManager):
    """Operator for clients"""
    def create_user(self, email, name, phone, address, password=None):
        """Create new client profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        if not phone:
            raise ValueError('User must have a phone number')
        
        if not address:
            raise ValueError('User must have an address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, address=address)
    
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, name, phone, address, password):
        """Create new superuser"""
        user = self.create_user(email, name, phone, address, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user
    

class Client(AbstractBaseUser, PermissionsMixin):
    """Database model for clients"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    
    objects = Operator()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'address']
    
    def get_name(self):
        """Return cleint full name"""
        return self.name
    
    def get_address(self):
        """Return cleint address"""
        return self.address
    
    def get_phone(self):
        """Return cleint phone number"""
        return self.phone
