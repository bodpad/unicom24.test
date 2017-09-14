from rest_framework import serializers
from api.models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'  # Для удобства все поля


class Request2coSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request2co
        fields = '__all__'  # Для удобства все поля
