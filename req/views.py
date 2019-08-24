from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import random,string
from req.models import (allReqs, req1, req2, req3, req4, req5, req6)
from . import serializers
from django.utils.timezone import now, timedelta
from licenses.views import getCar
# Create your views here.
def datecalc(x):
    return now() + timedelta(days=x)

def req1F(request, NID,NID2, ltype): #   path('1/<int:NID>/<int:NID2>/<int:ltype>', views.req1F),
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