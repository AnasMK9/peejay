from rest_framework import serializers
from licenses.models import car,driver
class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = '__all__'


class driverSerializer(serializers.ModelSerializer):
    class Meta:
        model = driver
        fields = '__all__'

        
    '''
    tarmeez = serializers.IntegerField
    Num
    owner
    cmake
    use
    category
    color
    yearModel
    reg_no
    chassis
    licenseExp
    passengers
    insuranceC
    insuranceP
    

 tarmeez = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    Num = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(99999)])
    owner = models.CharField(max_length=40)
    cmake = models.CharField(max_length = 15) #brand
    use = models.CharField(max_length=10) #sefat el est3mal
    category = models.CharField(max_length=10) #fe2at el markaba
    color = models.CharField(max_length = 20)
    yearModel = models.IntegerField(validators=[MaxValueValidator(2019), MinValueValidator(1990)])
    reg_no = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],primary_key=True)
    chassis = models.CharField(max_length=17,unique=True)
    licenseExp = models.DateField()
    passengers = models.IntegerField()
    insuranceC = models.CharField(max_length=15)
    insuranceP = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], unique=True)
'''


