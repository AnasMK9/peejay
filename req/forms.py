from django import forms
from . import models

class req1f(forms.Form): 
    NID =  forms.IntegerField(required=True)
    NID2 = forms.IntegerField(required=True)
    ltype = forms.IntegerField(required=True)
    '''
    class Meta:
        model = models.req1
        fields = ['NID', 'NID2','ltype']
    '''

class req2f(forms.Form): #/<int:NID>/<int:lno>/<int:deli>/<slug:addr>
    NID =  forms.IntegerField(required=True)
    lno = forms.IntegerField( required=True)
    deli = forms.IntegerField(required=True)
    addr = forms.CharField(required = True)

class req5f(forms.Form):
    NID = forms.IntegerField(required=True)
    tarmeez = forms.IntegerField(required=True)
    Num = forms.IntegerField(required=True)
    regNo = forms.IntegerField(required=True)
    deli = forms.IntegerField(required=True)
    addr = forms.CharField(required = True)
    

class req11f(forms.Form):#int:NID>/<int:NID2>/<slug:phone>/<int:tarmeez>/<int:Num>/<int:regNo
    NID =  forms.IntegerField(required=True)
    NID2 = forms.IntegerField(required=True)
    tarmeez = forms.IntegerField(required=True)
    Num = forms.IntegerField(required=True)
    regNo = forms.IntegerField(required=True)
    phone = forms.CharField(required = True)