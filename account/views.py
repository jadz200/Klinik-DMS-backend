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
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = AccountSerializer

    def post(self, request):
        data = request.data

        if(request.POST['password']==""):
            request.data._mutable = True
            request.POST['password']=UserManager().make_random_password()
            data._mutable = False

            
        if(request.POST['username']==""):
            request.data._mutable = True
            request.POST['username']=request.POST['email'].split('@')[0]
            data._mutable = False
        
        serializer = AccountSerializer(data = request.data)
        if(serializer.is_valid()):
            #message="Welcome to Klinic DMS, your password is :"+self.request.data['password']+"\n Hope to see you at work"
            #send_mail(
            #    'Welcome to Klinik DMS',
            #    message,
            #    settings.EMAIL_HOST_USER ,
            #    [self.request.data['email']],
            #    fail_silently=False
            #    )
            
            password = make_password(request.data['password'])
            serializer.save(password=password)
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "Account": serializer.data}, status=status.HTTP_201_CREATED
                )
        else:
            return Response({'ERROR': ('email may already exists')},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class ChangePasswordView(generics.UpdateAPIView):

    queryset = Account.objects.all()
    serializer_class = ChangePasswordSerializer
    

class UpdateProfileView(generics.UpdateAPIView):

    queryset = Account.objects.all()
    serializer_class = UpdateAccountSerializer    


