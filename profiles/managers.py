from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """"Create a new user"""
        if not email:
            raise ValueError('Please provide email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        """Create a new superuser"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff= True
        user.save(using=self._db)
        
        return user
    