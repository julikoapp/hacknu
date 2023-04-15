from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class ClientManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, phone, address, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(email=self.normalize_email(email), name=name, phone=phone, address=address)
    
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
    """Database model for users"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    
    objects = ClientManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'address']
    
    def __str__(self):
        """Return string representation"""
        return self.email


class Operator(models.Model):
    """Operator for users"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    
    def __str__(self):
        """Return string representation"""
        return self.email


class Brigada(models.Model):
    """Brigada model"""
    title = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        """Return string representation"""
        return self.email


class Task(models.Model):
    """Task model"""
    CATEGORIES = (
        (1, 'Install ecobox'),
        (2, 'Empty ecobox'),
        (3, 'Dismantle ecobox'),
    )
    STATUSES = (
        (1, 'Not started'),
        (2, 'In progress'),
        (3, 'Finished'),
    )
    status = models.IntegerField(choices=STATUSES, default=1)
    category = models.IntegerField(choices=CATEGORIES, default=1)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # client = models.ForeignKey(Client,  on_delete=models.CASCADE, related_name="client", null=True)
    client = models.TextField(null=True, blank=True)
    brigada = models.TextField(null=True, blank=True)
    # brigada = models.ForeignKey(Brigada,  on_delete=models.CASCADE, related_name="brigada", null=True)

    def __str__(self):
        return self.category
