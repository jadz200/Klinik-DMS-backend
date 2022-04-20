from django.db import models
from api.models  import *
from django.contrib.auth.models import AbstractBaseUser,UserManager
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  
from django_rest_passwordreset.signals import reset_password_token_created

# Create your models here.
class UserManager(UserManager):
  
  def create_user(self, email, password=None):
      
    user = self.model(email=self.normalize_email(email))

    user.set_password(password)
    user.save(using=self._db)
    return user

def create_staffuser(self, email, password):

      user = self.create_user(email,password=password)
      user.staff = True
      user.save(using=self._db)
      return user
  
def create_superuser(self, email, password):

      user = self.create_user(
          email,
          password=password,
      )
      user.staff = True
      user.admin = True
      user.save(using=self._db)
      return user
  
class Account(AbstractBaseUser):
    objects = UserManager() 
    email = models.EmailField(verbose_name='user email address', max_length=100, unique=True)
    username=models.CharField(max_length=50,default="")
    roleID=models.ForeignKey(Role,on_delete=models.CASCADE,null= True)

    is_active = models.BooleanField(default=True,null=False)
    is_staff = models.BooleanField(default=False,null=False)
    is_admin = models.BooleanField(default=False,null=False)
    is_superuser=models.BooleanField(default=False,null=False)
    password=models.CharField(max_length=100,)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        # users identification is by email
        return self.email

    def get_user_short_name(self):
        # user identification is by email
        return self.email

    def __str__(self):
        return (str(self.pk)+"   "+self.email)

    def has_perm(self, perm, obj=None):
        # return true if user has the necessary permissions
        return True
    
    def has_module_perms(self, app_label):
        # return true if user is granted the permission to view 'app_label'
        return True
    

