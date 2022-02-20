from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Doctor(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    mail= models.EmailField(max_length=254)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Patient(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    mail= models.EmailField(max_length=254)
    insurance= models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.first_name+" "+self.last_name

class Appointmemt(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    


class Receptionist(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    mail= models.EmailField(max_length=254)
    
    def __str__(self):
        return self.first_name+" "+self.last_name
    
class ClinicManager(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    mail= models.EmailField(max_length=254)
    
    def __str__(self):
        return self.first_name+" "+self.last_name
    
    