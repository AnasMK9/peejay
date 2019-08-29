from django import forms
from . import models

class req1f(forms.ModelForm): 
    '''NID =  forms.CharField(max_length=10, min_length= 10,required=True)
    NID2 = forms.CharField(max_length=10, min_length= 10,required=True)
    ltype = forms.IntegerField(required=True)
    '''
    class Meta:
        model = models.req1
        fields = ['NID', 'NID2','ltype']

    

    