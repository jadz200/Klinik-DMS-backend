from email import message
from email.message import EmailMessage
from rest_framework import generics, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.contrib.auth.models import UserManager
import uuid
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf  import settings
from .serializers import *
from api.views import *
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id
        token['first_name']=user.first_name
        token['last_name']=user.last_name
        token['email']=user.email
        token['phone']=user.phone

        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
