from pickle import TRUE
from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField
from datetime import datetime

# Create your models here.
class Clinic(models.Model):
    clinic_name = models.CharField(max_length=10, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clinic_name


class Role(models.Model):
    title=models.CharField(max_length=100,null= False, default="doctor")  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
  
   
class User(models.Model):
    first_name= models.CharField(max_length=20 ,  null = False)
    last_name= models.CharField(max_length=20,  null = False)
    phone = models.CharField(null=False,max_length=100)
    email = models.EmailField(verbose_name='user email address', max_length=100, unique=True)
    clinicID= models.ForeignKey(Clinic,on_delete=models.CASCADE , null=False)
    roleID=models.ForeignKey(Role,on_delete=models.CASCADE,null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    accountID= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Patient(models.Model):
    first_name= models.CharField(max_length=20 ,  null = False)
    last_name= models.CharField(max_length=20,  null = False)
    phone = models.CharField(null=False,max_length=100)
    mail = models.EmailField(verbose_name='user email address', max_length=100, unique=True)
    address=models.CharField(max_length=50, null=False, default="") 
    created_at = models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=90,null=True)
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
    clinicID= models.ForeignKey(Clinic,on_delete=models.CASCADE,null=False)
    title= models.CharField(max_length=100, null=False )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Appointment(models.Model):
    patientID=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    createdbyID=models.ForeignKey(User,default=1,on_delete=models.CASCADE, null=False,related_name="createdby")
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
    date=models.DateTimeField(null=False ,default=datetime(2022, 4, 9, 18, 43, 14, 109427))
    cost=MoneyField(decimal_places=2,default=0, default_currency='USD', max_digits=12,)
    comments= models.CharField(max_length=512,  null = True )
    created_at = models.DateTimeField(auto_now_add=True)

