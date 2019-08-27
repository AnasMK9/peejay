from django import forms
from . import models

class req1f(forms.Form):
    
    NID =  forms.IntegerField(required=True)
    NID2 = forms.IntegerField(required=True)
    ltype = forms.IntegerField(required=True)
    

    