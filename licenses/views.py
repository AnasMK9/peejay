from django.http import JsonResponse, HttpResponse
from licenses.models import car,driver
from datetime import date
import random
from licenses.serializers import driverSerializer, carSerializer
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
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
        if tarmeez > 10:
            if (car.objects.all().filter(tarmeez=tarmeez, Num=carNo).exists()) or (car.objects.all().filter(reg_no=regNo).exists()):
                return JsonResponse({"error": "Car doesn't Exist"})
            newcar = car(tarmeez=tarmeez, Num= carNo, reg_no=regNo)
            newcar.owner = request.user.fullname
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

@csrf_exempt
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

        return JsonResponse({"Message": "Bad Request"})
    
    
    '''
    
    
    
    
    
    
    
    
    dr = driver.objects.all().filter(NID=NID)
    serializer = driverSerializer(dr, many=True)
    return JsonResponse(serializer.data, safe=False)
    '''