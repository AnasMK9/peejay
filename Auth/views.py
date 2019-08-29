from django.contrib.auth import login, authenticate,get_user_model
from .models import Account
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from .forms import xform, loginF
from licenses.models import driver
from Auth.models import Account
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
@csrf_exempt
def signup(request):
    #return JsonResponse(, safe=False)
    if request.method == 'POST':
        form= xform(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            fullname = form.cleaned_data.get('fullname')
            user = authenticate(username=username, password=raw_password)
            return JsonResponse({'NID':user.NID, 'lno': driver.objects.get(NID = user.NID).licenseNo, 'fullname': fullname})
        else:
            return JsonResponse({'Message':'Something wrong happened'})
        
    else:
        form = xform()
        args = {'form' : form}
        return render(request, 'reg.html', args)
@csrf_exempt
def home(request):
    return HttpResponse("Nothing to see for humans here")

@csrf_exempt
def loginP(request):
    if request.method=="GET":
        form = loginF()
        args = {'form' : form}
        return render(request, 'reg.html', args)

    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            u = form.cleaned_data.get('username')
            p = form.cleaned_data.get('password')
            user = authenticate(username=u, password = p)
            if user:
                return JsonResponse({'NID':user.NID, 'lno': driver.objects.get(NID = user.NID).licenseNo, 'fullname': user.fullname})
            else:
                return JsonResponse({'Message': 'wrong login info'})
        else:
            return JsonResponse({'Message': form.data})

        



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