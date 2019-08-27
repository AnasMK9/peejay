from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import random,string
from req.models import (allReqs,reqT, req1, req2, req3, req4, req5, req6, req7, req11)
from . import serializers
from django.utils.timezone import now, timedelta
from licenses.views import getCar
from licenses.models import car
from Auth.models import Account
from collections import OrderedDict
import requests
from datetime import date
from . import forms
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def datecalc(x):
    return now() + timedelta(days=x)


@csrf_exempt
def req1F(request,NID,NID2,ltype): #<int:NID>/<int:NID2>/<int:ltype>
    
    if (NID2 < 5000000000 and NID2 > 1000000000):
        return JsonResponse({"Error":"الرقم الوطني ليس لقرابة من الدرجة الأولى"})
    elif (NID > 5000000000 and NID < 10000000000) or (NID2 > 5000000000 and NID2 < 10000000000):
        if req1.objects.filter(NID2 = NID2, NID= NID, ltype=ltype).count() > 0:
            return JsonResponse({"Error":"المعاملة مكررة"})
        else:
            reqid = ''.join(random.sample(string.ascii_lowercase, 10))
            newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 20, active = True,reqtype=1,expDate= datecalc(3))
            newReq2 = req1(NID = NID, paid = False, complete = False, req_id = reqid, price = 20, ltype = 32, NID2=NID2, expDate= datecalc(3), active = True ,reqtype=1) 
            newReq1.save()
            newReq2.save()
            final = req1.objects.all().filter(req_id = reqid)
            serializer = serializers.req1Serializer(final, many=True)
            return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"Error":"الرقم الوطني غير صحيح"})
@csrf_exempt
def req2F(request, NID,lno, deli,addr): #path('2/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req2F)
    if (NID > 1000000000 and NID < 10000000000):
            reqid = ''.join(random.sample(string.ascii_lowercase, 10))
            newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 12, active = True,reqtype=2,expDate= datecalc(1))
            newReq2 = req2(NID = NID, paid = False, complete = False, req_id = reqid, price = 12, lNo = lno, expDate= datecalc(1), active = True ,reqtype=2) 
            if deli == 1:
                newReq2.delivery = 'عن طريق البريد'
                newReq2.address = addr
            else:
                newReq2.delivery = 'استلام باليد'
                newReq2.address = 'مركز الترخيص'
            newReq1.save()
            newReq2.save()
            final = req2.objects.all().filter(req_id = reqid)
            serializer = serializers.req2Serializer(final, many=True)
            return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def req3F(request, NID,lno, deli,addr): #path('3/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req3F)
    if (NID > 1000000000 and NID < 10000000000):
            reqid = ''.join(random.sample(string.ascii_lowercase, 10))
            newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 8, active = True,reqtype=3,expDate= datecalc(2))
            newReq2 = req3(NID = NID, paid = False, complete = False, req_id = reqid, price = 8, lNo = lno, expDate= datecalc(2), active = True ,reqtype=3) 
            if deli == 1:
                newReq2.delivery = 'عن طريق البريد'
                newReq2.address = addr
            else:
                newReq2.delivery = 'استلام باليد'
                newReq2.address = 'مركز الترخيص'
            newReq1.save()
            newReq2.save()
            final = req3.objects.all().filter(req_id = reqid)
            serializer = serializers.req3Serializer(final, many=True)
            return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def req4F(request, NID,lno, deli,addr): #path('3/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req3F)
    if (NID > 1000000000 and NID < 10000000000):
            reqid = ''.join(random.sample(string.ascii_lowercase, 10))
            newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 32, active = True,reqtype=4,expDate= datecalc(2))
            newReq2 = req4(NID = NID, paid = False, complete = False, req_id = reqid, price = 32, lNo = lno, expDate= datecalc(2), active = True ,reqtype=4) 
            if deli == 1:
                newReq2.delivery = 'عن طريق البريد'
                newReq2.address = addr
            else:
                newReq2.delivery = 'استلام باليد'
                newReq2.address = 'مركز الترخيص'
            newReq1.save()
            newReq2.save()
            final = req4.objects.all().filter(req_id = reqid)
            serializer = serializers.req4Serializer(final, many=True)
            return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def req5F(request, NID,tarmeez, Num, regNo, deli, addr): #path('3/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req3F)
    reqid = ''.join(random.sample(string.ascii_lowercase, 10))
    newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 13, active = True,reqtype=5,expDate= datecalc(2))
    newReq2 = req5(NID = NID, paid = False, complete = False, req_id = reqid, price = 13, tarmeez = tarmeez, carNo=Num, regNo=regNo, expDate= datecalc(2), active = True ,reqtype=5) 
    if deli == 1:
        newReq2.delivery = 'عن طريق البريد'
        newReq2.address = addr
    else:
        newReq2.delivery = 'استلام باليد'
        newReq2.address = 'مركز الترخيص'
    newReq1.save()
    newReq2.save()
    final = req5.objects.all().filter(req_id = reqid)
    serializer = serializers.req5Serializer(final, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def req6F(request, NID,tarmeez, Num, regNo, deli, addr): #path('3/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req3F)
    reqid = ''.join(random.sample(string.ascii_lowercase, 10))
    newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 8, active = True,reqtype=6,expDate= datecalc(2))
    newReq2 = req6(NID = NID, paid = False, complete = False, req_id = reqid, price = 8, tarmeez = tarmeez, carNo=Num, regNo=regNo, expDate= datecalc(2), active = True ,reqtype=6) 
    if deli == 1:
        newReq2.delivery = 'عن طريق البريد'
        newReq2.address = addr
    else:
        newReq2.delivery = 'استلام باليد'
        newReq2.address = 'مركز الترخيص'
    newReq1.save()
    newReq2.save()
    final = req6.objects.all().filter(req_id = reqid)
    serializer = serializers.req6Serializer(final, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def req7F(request, NID,tarmeez, Num, regNo, deli, addr): #path('3/<int:NID>/<int:lno>/<int:deli>/<slug:addr>', views.req3F)
    reqid = ''.join(random.sample(string.ascii_lowercase, 10))
    newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 25, active = True,reqtype=7,expDate= datecalc(2))
    newReq2 = req7(NID = NID, paid = False, complete = False, req_id = reqid, price = 25, tarmeez = tarmeez, carNo=Num, regNo=regNo, expDate= datecalc(2), active = True ,reqtype=7) 
    if deli == 1:
        newReq2.delivery = 'عن طريق البريد'
        newReq2.address = addr
    else:
        newReq2.delivery = 'استلام باليد'
        newReq2.address = 'مركز الترخيص'
    newReq1.save()
    newReq2.save()
    final = req7.objects.all().filter(req_id = reqid)
    serializer = serializers.req7Serializer(final, many=True)
    return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def req11F(request,NID,NID2, phone,tarmeez, Num, regNo):
    reqid = ''.join(random.sample(string.ascii_lowercase, 10))
    if tarmeez < 10:
        return JsonResponse({"Error":"Car not found"})
    newcar = car(tarmeez=tarmeez, Num= Num, reg_no=regNo)
    newcar.owner = Account.objects.get(pk=request.user.NID).fullname
    newcar.cmake = random.choice(['Mitsubishi', 'McLaren','Lexus', 'Bentley' , 'Mazda','Suzuki', 'Subaru', 'Volkswagen', 'Jeep', 'Lamborghini', 'Porsche', 'Toyota', 'Ferrari', 'Mercedes', 'Audi', 'Ford', 'Honda', 'BMW', 'Hyundai', 'KIA'])
    newcar.color = random.choice(['Red', 'Green', 'Yellow', 'Blue', 'range', 'Purple', 'Cyan', 'Magenta', 'Lime', 'Pink', 'Lavender', 'Brown', 'Beige', 'Maroon', 'Mint', 'live', 'Apricot', 'Navy', 'Grey', 'White', 'Black'])
    newcar.yearModel = random.randint(1990,2019)
    newcar.chassis =requests.get('http://www.randomvin.com/getvin.php?type=real').text
    newcar.insuranceP = random.randint(20000000,80000000)
    newcar.insuranceC = 'Insurance Company'
    newcar.passengers = random.choice([4,5])
    newcar.licenseExp = date(random.randint(2018,2023), random.randint(1,12), random.randint(1,28))
    newcar.use = 'ركوب'
    newcar.category = random.choice(['ركوب كبير', 'ركوب صغير'])
    if (newcar.licenseExp - date.today()).days < 30 :
        newcar.renew = True
    else:
        newcar.renew = False
    newcar.save()
    newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 25, active = True,reqtype=11,expDate= datecalc(1))
    newReq2 = req11(NID = NID, paid = False, complete = False, req_id = reqid,phone = phone, NID2 =NID2 , price = 25, tarmeez = tarmeez, carNo=Num, regNo=regNo, expDate= datecalc(1), active = True ,reqtype=11) 
    newReq1.save()
    newReq2.save()
    final = req11.objects.all().filter(req_id = reqid)
    serializer = serializers.req11Serializer(final, many=True)
    return JsonResponse(serializer.data, safe=False)

'''
    pickup_dict = {}
    pickup_records=[]
    for tmpPickUp in pickup:
        pickup_date=tmpPickUp.pickup_date
        pickup_time=tmpPickUp.pickup_time
        pickup_id = tmpPickUp.id
        pickup_name=tmpPickUp.customer_name
        pickup_number=tmpPickUp.pieces
        print pickup_date,pickup_time,pickup_id,pickup_name,pickup_number
        record = {"name":pickup_name, "id":pickup_id,"number":pickup_number,"status":"1","time":"time"}
        print record
        pickup_records.append(record)
    pickup_dict["pickup"]=pickup_records
    return JsonResponse(pickup_dict)
'''
@csrf_exempt
def getAll(request, NID):
    res = []
    res.append(serializers.req1Serializer(req1.objects.filter(NID = NID),many=True).data)
    res.append(serializers.req2Serializer(req2.objects.filter(NID = NID),many=True).data)
    res.append(serializers.req3Serializer(req3.objects.filter(NID = NID),many=True).data)
    res.append(serializers.req4Serializer(req4.objects.filter(NID = NID),many=True).data)
    res.append(serializers.req5Serializer(req5.objects.filter(NID = NID),many=True).data)
    res.append(serializers.req6Serializer(req6.objects.filter(NID = NID),many=True).data)
    res.append(serializers.req7Serializer(req7.objects.filter(NID = NID),many=True).data)
    res.append(serializers.req11Serializer(req11.objects.filter(NID = NID),many=True).data)

    return JsonResponse(res, safe = False)
@csrf_exempt
def payAll(request, NID):
    allReqs.objects.filter(NID=NID).update(paid = True)
    req1.objects.filter(NID = NID).update(paid = True)
    req2.objects.filter(NID = NID).update(paid = True)
    req3.objects.filter(NID = NID).update(paid = True)
    req4.objects.filter(NID = NID).update(paid = True)
    req5.objects.filter(NID = NID).update(paid = True)
    req6.objects.filter(NID = NID).update(paid = True)
    req7.objects.filter(NID = NID).update(paid = True)
    req11.objects.filter(NID = NID).update(paid = True)

    return JsonResponse({"Message" : "Success"})
@csrf_exempt
def payone(request, ID):
    allReqs.objects.filter(req_id= ID).update(paid = True)

    allReqs.objects.filter(req_id= ID).update(paid = True)
    req1.objects.filter(req_id= ID).update(paid = True)
    req2.objects.filter(req_id= ID).update(paid = True)
    req3.objects.filter(req_id= ID).update(paid = True)
    req4.objects.filter(req_id= ID).update(paid = True)
    req5.objects.filter(req_id= ID).update(paid = True)
    req6.objects.filter(req_id= ID).update(paid = True)
    req7.objects.filter(req_id= ID).update(paid = True)
    req11.objects.filter(req_id= ID).update(paid = True)

    return JsonResponse({"Message" : "Success"})
#>>> from req.models import allReqs
#>>> from req.models import allReqsSerializer