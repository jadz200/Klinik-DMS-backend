from pyexpat import model
from django.db import models
from api.models  import *
from django.contrib.auth.models import AbstractBaseUser,UserManager
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  

# Create your models here.
