from pickle import FALSE
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

    def create_user(self, email, password=None,is_staff=False,is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_staff=is_staff
        user.is_admin=is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self,email,password=None):
        user=self.create_user(email,password,is_staff=True,is_admin=True)
        user.save(using=self._db)


    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
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


    def get_full_name(self):
        return self.first_name+" "+self.last_name

    def get_user_short_name(self):
        # user identification is by email
        return self.first_name

    def __str__(self):
        return self.first_name+" "+self.last_name

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
    mail = models.EmailField(verbose_name='Email address', max_length=100, unique=True)
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
    patientID=models.ForeignKey(Patient, on_delete=models.CASCADE,verbose_name="Patient")
    doctorID=models.ForeignKey(User, on_delete=models.CASCADE,null=True,verbose_name="Doctor")
    roomID=models.ForeignKey(Room, on_delete=models.CASCADE, null=True,verbose_name="Room")
    date=models.DateTimeField(null=False,)
    duration= models.IntegerField(null=False, default=0)
    reason=models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.date)[0:16]+" "+str(self.patientID)+" "

class Operation(models.Model):
    title=models.CharField(max_length=50 ,verbose_name="Operation")
    cost=MoneyField(decimal_places=2, default_currency='USD', max_digits=12,verbose_name="Default Price")
    def __str__(self):
        return self.title


class Visit(models.Model):
    patientID=models.ForeignKey(Patient, on_delete=models.CASCADE,null=False,default=1,verbose_name="Patient")
    doctorID=models.ForeignKey(User, on_delete=models.CASCADE,null=True, verbose_name="Doctor")
    roomID=models.ForeignKey(Room, on_delete=models.CASCADE,null=False,verbose_name="Room")
    date=models.DateTimeField(auto_now_add=True)
    cost=MoneyField(decimal_places=2,default=0, default_currency='USD', max_digits=12,)
    comments= models.CharField(max_length=512,  null = True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.date)[0:16]+" "+str(self.patientID)+" "

class Visit_Operation(models.Model):
    operation=models.ForeignKey(Operation,on_delete=models.CASCADE,null= True)    
    cost=MoneyField(decimal_places=2, default_currency='USD', max_digits=12,verbose_name="Price")
    visitID=models.ForeignKey(Visit, on_delete=models.CASCADE)