from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password= None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
    
        user = self.model(
            email= self.normalize_email(email),
            username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email           = models.EmailField(max_length=60, verbose_name='email' , unique=True)
    username        = models.CharField(max_length=30, unique=True)
    dateJoined      = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
    lastLogin       = models.DateTimeField(auto_now=True, verbose_name='last login')
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superuser    = models.BooleanField(default=False)
    name = models.CharField(max_length=60, verbose_name="full name")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.email + ", " + self.username 

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True