from django.shortcuts import render
from rest_framework import viewsets

from API.serializers import UserSerializer
from HealthRecord.models import H_User

# Create your views here.

class HealthViewSet(viewsets.ModelViewSet):

    queryset = H_User.objects.all().order_by('id')
    serializer_class = UserSerializer
 