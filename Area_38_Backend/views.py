from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import LoginSerializer

class LoginList(APIView):
    def get(self, request, format=None):
        loginKits = User.objects.all()[0:5] # change table name
        serializer = LoginSerializer(loginKits, many=True)
        return Response(serializer.data)
