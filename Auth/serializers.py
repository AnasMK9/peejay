from rest_framework import serializers
from .models import Account

class loginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username', 'password']