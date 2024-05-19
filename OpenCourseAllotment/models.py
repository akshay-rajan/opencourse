from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom user model"""
    
    is_teacher = models.BooleanField(default=False)
    # USERNAME_FIELD = 'username  '
    # REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
