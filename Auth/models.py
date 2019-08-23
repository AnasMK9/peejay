from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
class AccountManager(BaseUserManager):
    def Create_user(self, fullname,NID,phone,email,username,password):
        if (not email or not fullname or not NID or not phone or not email or not username or not password):
            raise ValueError('Incomplete registration info')
        AccountOb = self.model(
            email = self.normalize_email(email)
        )
        AccountOb.fullname = fullname
        AccountOb.NID=NID
        AccountOb.phone = phone 
        AccountOb.username = username
        AccountOb.set_password(password)
        AccountOb.is_staff = False
        AccountOb.is_superuser = False
        AccountOb.is_active = True

        AccountOb.save(using=self._db)


        return AccountOb


    def create_superuser(self, fullname,NID,phone,email,username,password, is_staff):
        if (not email or not fullname or not NID or not phone or not email or not username or not password):
            raise ValueError('Incomplete registration info')
        AccountOb = self.model(
            email = self.normalize_email(email)
        )
        AccountOb.fullname = fullname
        AccountOb.NID=NID
        AccountOb.phone = phone 
        AccountOb.username = username
        AccountOb.set_password(password)
        AccountOb.is_staff = True
        AccountOb.is_superuser = True
        AccountOb.is_active = True
        
        AccountOb.save(using=self._db)

        return AccountOb

    
class Account(AbstractBaseUser,PermissionsMixin):
    fullname = models.CharField(max_length=50)
    NID = models.CharField(validators=[RegexValidator(regex='^.{10}$', message='Please enter a valid national ID', code='1')],primary_key=True, max_length=10) #National ID
    phone = models.CharField(validators=[RegexValidator(regex='^.{10}$', message='Please enter a valid number', code='3')], max_length=10,unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=15, unique=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname', 'NID', 'phone', 'email', 'password', 'is_staff']
    objects = AccountManager()

    
