from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser,UserManager, PermissionsMixin


# Create your models here.
class Clinic(models.Model):
    clinic_name = models.CharField(max_length=10, null=False,verbose_name="Clinic")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clinic_name


class Role(models.Model):
    title=models.CharField(max_length=100,null= False, default="doctor")  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserManager(UserManager):
  
    def create_user(self, email, password=None,**kwargs):
        if not email:
            raise ValueError('Email field is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        
    def create_staffuser(self, email, password,):

      user = self.create_user(email,password=password )
      user.staff = True
      user.save(using=self._db)
      return user
  
    def create_superuser(self, email, password,):

          user = self.create_user(
              email,
              password=password,
          )
          user.staff = True
          user.admin = True
          user.save(using=self._db)
          return user  
    
class User(AbstractBaseUser,PermissionsMixin):
    objects = UserManager() 
    first_name= models.CharField(max_length=20 ,  null = False)
    last_name= models.CharField(max_length=20,  null = False)
    phone = models.CharField(null=False,verbose_name='Phone number',max_length=100)
    email = models.EmailField(verbose_name='Email address', max_length=100, unique=True)
    clinicID= models.ForeignKey(Clinic,verbose_name='Clinic',on_delete=models.CASCADE , null=True)
    roleID=models.ForeignKey(Role,verbose_name='Role',on_delete=models.CASCADE,null= True)
    username=models.CharField(max_length=50)
    is_active = models.BooleanField(default=True,null=False)
    is_staff = models.BooleanField(default=False,null=False)
    is_admin = models.BooleanField(default=False,null=False)
    is_superuser=models.BooleanField(default=False,null=False)
    
    password=models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def get_full_name(self):
        # users identification is by email
        return self.email

    def get_user_short_name(self):
        # user identification is by email
        return self.email

    def __str__(self):
        return (self.email)

    def has_perm(self, perm, obj=None):
        # return true if user has the necessary permissions
        return True
    
    def has_module_perms(self, app_label):
        # return true if user is granted the permission to view 'app_label'
        return True
    




class Patient(models.Model):
    first_name= models.CharField(max_length=20 ,  null = False)
    last_name= models.CharField(max_length=20,  null = False)
    phone = models.CharField(null=False,max_length=100)
    mail = models.EmailField(verbose_name='user email address', max_length=100, unique=True)
    address=models.CharField(max_length=50, null=False, default="") 
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name+" "+self.last_name
    
    
class JournalEntryType(models.Model):
    title=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class PaymentJournal(models.Model):
    patientID=models.ForeignKey(Patient, null= False,on_delete=models.CASCADE)
    journal_entry_typeID=models.ForeignKey(JournalEntryType, null=False,on_delete=models.CASCADE)
    clinicID=models.ForeignKey(Clinic,null=False,on_delete=models.CASCADE)
    amount=MoneyField(decimal_places=2,default=0, default_currency='USD', max_digits=12,)
    reason=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
    clinicID= models.ForeignKey(Clinic,on_delete=models.CASCADE,null=False,verbose_name="Clinic")
    title= models.CharField(max_length=100, null=False, verbose_name="Room title")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Appointment(models.Model):
    patientID=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctorID=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="doctor")
    roomID=models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    date=models.DateTimeField(null=False,default=datetime(2022, 4, 9, 18, 43, 14, 109427))
    duration= models.IntegerField(null=False, default=0)
    reason=models.CharField(max_length=255, null=False,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.date +" "+self.patientID+" "+self.doctorID

class Visit(models.Model):
    patientID=models.ForeignKey(Patient, on_delete=models.CASCADE,null=False,default=1)
    doctorID=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    roomID=models.ForeignKey(Room, on_delete=models.CASCADE,null=False)
    date=models.DateTimeField(auto_now_add=True)
    cost=MoneyField(decimal_places=2,default=0, default_currency='USD', max_digits=12,)
    comments= models.CharField(max_length=512,  null = True )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.patientID+" "+self.doctorID+" "+self.roomID