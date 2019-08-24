from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import random,string
from req.models import (allReqs,req1)
from . import serializers
from django.utils.timezone import now, timedelta
# Create your views here.
def datecalc(x):
    return now() + timedelta(days=x)

def req1F(request, NID,NID2, ltype):
    if (NID2 < 5000000000 and NID2 > 1000000000):
        return JsonResponse({"Error":"الرقم الوطني ليس لقرابة من الدرجة الأولى"})
    elif (NID > 5000000000 and NID < 10000000000) or (NID2 > 5000000000 and NID2 < 10000000000):
        if req1.objects.filter(NID2 = NID2, NID= NID, ltype=ltype).exists():
            return JsonResponse({"Error":"المعاملة مكررة"})
        else:
            reqid = ''.join(random.sample(string.ascii_lowercase, 10))
            newReq1 = allReqs(NID = NID, paid = False, complete = False, req_id = reqid, price = 20, active = True,reqtype=1)
            newReq2 = req1(NID = NID, paid = False, complete = False, req_id = reqid, price = 20, ltype = 32, NID2=NID2, expDate= datecalc(3), active = True ,reqtype=1) 
            newReq1.save()
            newReq2.save()
            final = req1.objects.all().filter(req_id = reqid)
            serializer = serializers.req1Serializer(final, many=True)
            return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"Error":"الرقم الوطني غير صحيح"})
