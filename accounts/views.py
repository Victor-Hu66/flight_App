from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView

class RegisterApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    