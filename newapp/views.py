from models import User , Rent , Electricity
from serializers import UserSerializer , RentSerializer , ElectricitySerializer
from rest_framework import generics

class CreateAPIView(generics.GenericAPIView):
    