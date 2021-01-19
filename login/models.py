from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django_resized import ResizedImageField



class CustomUserManager(BaseUserManager):
    # Create a new user with the specified fields
    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        # If email or password were not provided, throw an exception
        if not (email and password):
            raise ValueError('User must have an email address and password.')
        # Make the email not case-sensitive
        email = self.normalize_email(email)
        # Start creating the user with the fields
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        # Hash the password
        user.set_password(password)
        # All users are superusers in VMC-TAP
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        # Create DB entry and return the user object
        user.save()
        return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True, primary_key=True)
    is_superuser = models.BooleanField(default=True)
    avatar = ResizedImageField(quality=100, size=[120, 120], upload_to='profile_pic', blank=True)

    USERNAME_FIELD = 'email'

    # This should contain the required fields that are not email or password (those are
    # already required)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'avatar']

    objects = CustomUserManager()

    def __str__(self):
        return self.email



