from rest_framework.serializers import ModelSerializer
from .models import allReqs, req1

class req1Serializer(ModelSerializer):
    class Meta:
        model = req1
        fields = '__all__'