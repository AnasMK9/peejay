from django.contrib.auth import login, authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse

from django.http import HttpResponse

response_data = {}
response_data['result'] = 'error'
response_data['message'] = 'Some error message'

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'Message':'Success'})
        else:
            return JsonResponse({'message':'Pathetic'})
    else:
        form = UserCreationForm()
        args = {'form' : form}
        return render(request, 'reg.html', args)


'''
            NID = form.cleaned_data.get('NID')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=NID, password=raw_password)
            login(request, user)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Some error message'
        return (response_data)
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    return (response_data)
'''