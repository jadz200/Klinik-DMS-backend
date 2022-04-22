from pyexpat import model
from django.db import models
from api.models  import *
from django.contrib.auth.models import AbstractBaseUser,UserManager
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  
from django_rest_passwordreset.signals import reset_password_token_created

# Create your models here.
