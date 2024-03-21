from rest_framework import serializers
from .models import Rent, Electricity, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', "email"]

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'

class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Electricity
        fields = '__all__'