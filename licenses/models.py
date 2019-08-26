from django.db import models
from Auth.models import Account
import random
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator

# Create your models here.


class car(models.Model):
    tarmeez = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    Num = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(99999)])
    owner = models.CharField(max_length=40)
    cmake = models.CharField(max_length = 15) #brand
    use = models.CharField(max_length=10) #sefat el est3mal
    category = models.CharField(max_length=10) #fe2at el markaba
    color = models.CharField(max_length = 20)
    yearModel = models.IntegerField(validators=[MaxValueValidator(2019), MinValueValidator(1990)])
    reg_no = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],primary_key=True)
    chassis = models.CharField(max_length=17,unique=True)
    licenseExp = models.DateField()
    passengers = models.IntegerField()
    insuranceC = models.CharField(max_length=15)
    insuranceP = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], unique=True)
    renew = models.BooleanField(default=False)
    objects = models.Manager()
    

    class Meta:
        unique_together =  ('tarmeez', 'Num')

class driver(models.Model):
    fullname = models.CharField(max_length=50)
    NID = models.IntegerField(validators=[MinValueValidator(1000000000, MaxValueValidator(9999999999))], ) #National ID
    licenseNo = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], default= random.randint(30000000,80000000), primary_key=True)
    issueDate = models.DateField(date(random.randint(2006,2016), random.randint(1,12), random.randint(1,28)))
    expDate = models.DateField(default = date(random.randint(2015,2019), random.randint(9,12), random.randint(1,28)))
    center = models.CharField(max_length = 10, default='مركز ترخيص')
    ltype = models.IntegerField(default=32)
    renew = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.fullname
