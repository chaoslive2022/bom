from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from profiles import managers

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Custom user class"""
    email = models.EmailField(max_length=255, unique=True, error_messages={'unique': 'This email already exists'})
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = managers.UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    #class Meta:
    #    ordering = ('name',)

    def __str__(self):
        return self.email


