from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings


class Client(AbstractBaseUser, PermissionsMixin):
    """Database model for clients"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'address']
    
    def create_user(self, email, name, phone, address, password):
        """Create new user profile"""
        if not email:
            raise ValueError('Client must have an email address')
        
        if not password:
            raise ValueError('Client must have a password')
        
        if not address:
            raise ValueError('Client must have an address')
        
        user = self.model(email=email, name=name, phone=phone, address=address)
    
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def __str__(self):
        """Return string representation"""
        return self.email


class Operator(models.Model):
    """Operator for users"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True)

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
    TYPES = (
        (1, 'Install ecobox'),
        (2, 'Empty ecobox'),
        (3, 'Dismantle ecobox'),
    )
    STATUSES = (
        (1, 'Not started'),
        (2, 'In progress'),
        (3, 'Finished'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=255, choices=TYPES)
    status = models.CharField(max_length=255, choices=STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
