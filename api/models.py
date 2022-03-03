from re import T
from django.db import models
from djmoney.models.fields import MoneyField
from datetime import datetime    

# Create your models here.
class Clinic(models.Model):
    clinic_name = models.CharField(max_length=10, null=False)


class Role(models.Model):
    title=models.CharField(max_length=100,null= False, default="doctor")    
   
class User(models.Model):
    clinicID= models.ForeignKey(Clinic,on_delete=models.CASCADE , null=False)
    roleID=models.ForeignKey(Role,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=20 ,  null = False)
    last_name= models.CharField(max_length=20,  null = False)
    phone = models.IntegerField(null=False,  unique=True )
    mail= models.EmailField(max_length=30 , null = False , blank = False)
    
    def __str__(self):
        return self.first_name+" "+self.last_name
class Patient(models.Model):
    first_name= models.CharField(max_length=20 ,  null = False)
    last_name= models.CharField(max_length=20,  null = False)
    phone = models.IntegerField(null=False,  unique=True )
    mail= models.EmailField(max_length=30 , null = False , blank = False)
    address=models.CharField(max_length=50, null=False, default="") 

class JournalEntryType(models.Model):
    title=models.CharField(max_length=255)

class PaymentJournal(models.Model):
    patientID=models.ForeignKey(Patient, null= False,on_delete=models.CASCADE)
    journal_entry_typeID=models.ForeignKey(JournalEntryType, null=False,on_delete=models.CASCADE)
    clinicID=models.ForeignKey(Clinic,null=False,on_delete=models.CASCADE)
    userID=models.ForeignKey(User,null=False, on_delete=models.CASCADE)
    amount=MoneyField(decimal_places=2,default=0, default_currency='USD', max_digits=12,)
    reason=models.CharField(max_length=255)

class Room(models.Model):
    clinicID= models.ForeignKey(Clinic,on_delete=models.CASCADE,null=False)
    title= models.CharField(max_length=100, null=False )


class Appointment(models.Model):
    patientID=models.ForeignKey(Patient, on_delete=models.CASCADE)
    createdbyID=models.ForeignKey(User,default=1,on_delete=models.CASCADE, null=False,related_name="createdby")
    doctorID=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="doctor")
    roomID=models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    date=models.DateTimeField(null=False,default=datetime.now())
    duration= models.IntegerField(null=False, default=0)
    reason=models.CharField(max_length=255, null=False,default="")
    
class Visit(models.Model):
    patientID=models.ForeignKey(Patient, on_delete=models.CASCADE,null=False,default=1)
    doctorID=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    roomID=models.ForeignKey(Room, on_delete=models.CASCADE,null=False)
    date=models.DateTimeField(null=False ,default=1)
    cost=MoneyField(decimal_places=2,default=0, default_currency='USD', max_digits=12,)
    comments= models.CharField(max_length=512,  null = True )

class Operation(models.Model):
    clinicID= models.ForeignKey(Clinic,on_delete=models.CASCADE , null=False)
    title= models.CharField(max_length=100, null=False )
    cost=MoneyField(decimal_places=2,default=0, default_currency='USD', max_digits=12,)
    
class Visit_Operation(models.Model):
    visitID= models.ForeignKey(Visit,on_delete=models.CASCADE , null=False)
    operationID= models.ForeignKey(Operation,on_delete=models.CASCADE , null=False)
    cost=MoneyField(decimal_places=2,default=0, default_currency='USD', max_digits=12,)
