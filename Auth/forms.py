from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator, EmailValidator
from .models import Account
from django.db import models
from licenses.models import driver
from datetime import date
from random import randint
class xform(forms.ModelForm):

    email = forms.EmailField(required=True)
    fullname = forms.CharField(required=True)
    NID = forms.CharField(required=True)
    username = forms.CharField(required=True)

    phone = forms.CharField(required=True)
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['fullname', 'NID','username', 'phone', 'email', 'password']
    
    

    def save(self, commit=True):
        user = super(xform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.fullname = self.cleaned_data['fullname']
        user.username = self.cleaned_data['username']
        user.NID = self.cleaned_data['NID']
        user.phone = self.cleaned_data['phone']
        user.set_password(self.cleaned_data["password"])
        user.is_active = True
        user.save(commit)
        newD = driver(fullname = self.cleaned_data['fullname'],NID = self.cleaned_data['NID'])
        # , expDate = date(randint(2015,2019), randint(9,12), randint(1,28))
        newD.ltype = 32
        newD.center = ' مركز ترخيص'
        newD.licenseNo = randint(10000000,99999999)
        newD.issueDate = date(randint(2006,2016), randint(1,12), randint(1,28))
        newD.expDate = date(randint(2015,2019), randint(9,12), randint(1,28))
        newD.save()
        

        
        if commit:
            user.save()

        return user

class loginF(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
    
    
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    '''