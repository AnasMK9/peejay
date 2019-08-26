from rest_framework.serializers import ModelSerializer
from .models import allReqs, req1,req2,req3,req4,req5,req6,req7,req11

class req1Serializer(ModelSerializer):
    class Meta:
        model = req1
        fields = '__all__'

class allReqserializer(ModelSerializer):
    class Meta:
        model = allReqs
        fields = '__all__'

class req2Serializer(ModelSerializer):
    class Meta:
        model = req2
        fields = '__all__'

class req3Serializer(ModelSerializer):
    class Meta:
        model = req3
        fields = '__all__'
class req4Serializer(ModelSerializer):
    class Meta:
        model = req4
        fields = '__all__'

class req5Serializer(ModelSerializer):
    class Meta:
        model = req5
        fields = '__all__'


class req6Serializer(ModelSerializer):
    class Meta:
        model = req6
        fields = '__all__'

class req7Serializer(ModelSerializer):
    class Meta:
        model = req7
        fields = '__all__'

class req11Serializer(ModelSerializer):
    class Meta:
        model = req11
        fields = '__all__'