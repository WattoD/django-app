from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


# Create your models here.
class Message(models.Model):
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('members.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}: {self.value}'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='phone number')
    first_name = models.CharField(max_length=30, verbose_name='first name', blank=True)
    last_name = models.CharField(max_length=30, verbose_name='last name', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='active')
    is_staff = models.BooleanField(default=False, verbose_name='staff')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='registration date')

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        permissions = [
            ("can_view_sensitive_data", "Can view confidential data"),
            ("can_export_users", "Can export users"),
        ]

    def __str__(self):
        return f'{self.email}: {self.registration_date}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

