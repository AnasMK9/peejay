from rest_framework.generics import RetrieveAPIView
from django.http import JsonResponse, HttpResponse
from licenses.models import car,driver
from Auth.models import Account
from datetime import date
import random
from licenses.serializers import driverSerializer, carSerializer
import requests

# Create your views here.

def getCar(request, tarmeez, carNo, regNo):
    #carr = car.objects.filter(reg_no=regNo, tarmeez=tarmeez, Num=carNo).values_list()
    if tarmeez > 20 or carNo > 99999 or regNo > 9999999999:
        return JsonResponse({"error": "Car doesn't Exist"})
    elif car.objects.all().filter(reg_no=regNo, tarmeez=tarmeez, Num=carNo).exists():
        carr = car.objects.get(reg_no=regNo) #, tarmeez=tarmeez, Num=carNo
        
        per = carr.licenseExp - date.today()
        if per.days < 30:
            carr.renew = True
            carr.save()
        final = car.objects.all().filter(reg_no=regNo, tarmeez=tarmeez, Num=carNo)
        serializer = carSerializer(final, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        if random.choice([True,False]):
            
            if (car.objects.all().filter(tarmeez=tarmeez, Num=carNo).exists()) or (car.objects.all().filter(reg_no=regNo).exists()):
                return JsonResponse({"error": "Car doesn't Exist"})
            newcar = car(tarmeez=tarmeez, Num= carNo, reg_no=regNo)
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
            final = car.objects.all().filter(reg_no=regNo, tarmeez=tarmeez, Num=carNo)
            serializer = carSerializer(final, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"error": "Car doesn't Exist"})


def getDriver(request,NID):
    if NID > 9999999999 or NID < 1000000000:
        return JsonResponse({"error": "Please enter a valid National ID"})
    elif driver.objects.all().filter(NID=NID).exists():
        driverr = driver.objects.get(NID=NID) 
        
        per = driverr.expDate - date.today()
        if per.days < 30:
            driverr.renew = True
            driverr.save()
        final = driver.objects.all().filter(NID=NID)
        serializer = driverSerializer(final, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        #newD = driver(NID=Account.objects.get(pk=request.user.NID).NID)
        newD = driver(NID=NID)
        newD.fullname = Account.objects.get(pk=request.user.NID).fullname
        newD.licenseNo = random.randint(30000000,80000000)
        newD.issueDate = date(random.randint(2006,2016), random.randint(1,12), random.randint(1,28))
        newD.expDate = date(random.randint(2015,2019), random.randint(9,12), random.randint(1,28))
        newD.center = 'مركز ترخيص'
        newD.ltype = 32
        per = newD.expDate - date.today()
        if (newD.expDate - date.today()).days < 30:
            newD.renew = True
        newD.save()
        final = driver.objects.all().filter(NID=NID)
        serializer = driverSerializer(final, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    '''
    else:
        if random.choice([True,False]):
            
            if (car.objects.all().filter(NID=NID, licenseNo=Lno).exists()) or (car.objects.all().filter(reg_no=regNo).exists()):
                return JsonResponse({"error": "Please enter a valid License Number/National ID"})
            newcar = car(tarmeez=tarmeez, Num= carNo, reg_no=regNo)
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
            final = car.objects.all().filter(reg_no=regNo, tarmeez=tarmeez, Num=carNo)
            serializer = driverSerializer(final, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"error": "Please enter a valid License Number/National ID"})
    
    '''
    
    
    
    
    
    
    
    
    dr = driver.objects.all().filter(NID=NID)
    serializer = driverSerializer(dr, many=True)
    return JsonResponse(serializer.data, safe=False)
