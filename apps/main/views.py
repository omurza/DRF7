from django.shortcuts import render
from rest_framework import viewsets
from .models import UsersModel,TaskModel 
from .serializers import UsersSerializer,TaskSerializer
# Create your views here.
class UserViewApi(viewsets.ModelViewSet):
    queryset=UsersModel.objects.all()
    serializer_class=UsersSerializer

class TaskViewApi(viewsets.ModelViewSet):
    queryset=TaskModel.objects.all()
    serializer_class=TaskSerializer