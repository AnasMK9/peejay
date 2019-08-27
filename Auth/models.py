from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator,MaxValueValidator
from licenses.models import driver
from datetime import date
from random import randint
# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, fullname,NID,phone,email,username,password):
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
        newD = driver(fullname = fullname, NID = NID)
        # , expDate = date(randint(2015,2019), randint(9,12), randint(1,28))
        newD.ltype = 32
        newD.center = ' مركز ترخيص'
        newD.licenseNo = randint(10000000,99999999)
        newD.issueDate = date(randint(2006,2016), randint(1,12), randint(1,28))
        newD.expDate = date(randint(2015,2019), randint(9,12), randint(1,28))
        newD.save()



        AccountOb.save(using=self._db)


        return AccountOb


    def create_superuser(self, fullname,NID,phone,email,username,password):
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
    NID = models.IntegerField(validators=[MinValueValidator(1000000000, MaxValueValidator(9999999999))],primary_key=True ) #National ID
    phone = models.CharField(validators=[RegexValidator(regex='^.{10}$', message='Please enter a valid number', code='3')], max_length=10,unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    password = models.CharField(max_length= 50)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname', 'NID', 'phone', 'email', 'password']
    objects = AccountManager()

    
