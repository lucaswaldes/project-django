from django.db import models

from .managers import UserAuthManager
from base.models import BaseModel, SoftDelete

from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)
import uuid
import datetime

from django.utils import timezone
from datetime import timedelta
import pytz

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.is_staff = True
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_client(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.is_staff = False
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    def create_new_discord_user(self, user):
        print('Inside Discord User Manager')
        discord_tag = '%s#%s' % (user['username'], user['discriminator'])
        new_user = self.create(
            username=user['username'],
            discord_id=user['id'],
            avatar=user['avatar'],
            email=user['email'],
            public_flags=user['public_flags'],
            flags=user['flags'],
            locale=user['locale'], 
            mfa_enabled=user['mfa_enabled'],
            discord_tag=discord_tag
        )
        return new_user

class DiscordUser(AbstractUser):
    
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    discord_id = models.CharField(max_length=100, null=True, blank=True, unique=False)
    discord_tag = models.CharField(max_length=100, null=True, blank=True, unique=False)
    email = models.EmailField(("email address"), blank=False, unique=True)
    avatar = models.CharField(max_length=100, null=True, blank=True)
    public_flags = models.IntegerField(null=True, blank=True)
    flags = models.IntegerField(null=True, blank=True)
    locale = models.CharField(max_length=100, null=True, blank=True)
    mfa_enabled = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    token = models.CharField(max_length=500)
    auth_provider = models.CharField(max_length=50)
    last_login = models.DateTimeField(default=timezone.now)


    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]

    # def is_authenticated(self, request):
    #     return True

    def has_perm(self, perm, obj=None):
            return self.is_admin

    def has_module_perms(self, app_label):
            return self.is_admin

    # def is_login_expired(self):
    #     expiration_time = self.last_login + timedelta(minutes=2)
    #     current_time = timezone.now()
    #     expiration_time_fixed = expiration_time - timedelta(hours=3)  # Ajuste de deslocamento de tempo fixo (exemplo: -03:00)
    #     return current_time > expiration_time_fixed