from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Role(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Moderator', 'Moderator'),
        ('User', 'User'),
    ]
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
    permissions = models.TextField(help_text="Comma-separated list of permissions")

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def has_permission(self, permission):
        if not self.role:
            return False
        return permission in self.role.permissions.split(',')
    
    
