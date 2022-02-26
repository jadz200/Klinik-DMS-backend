from django.db import models



# Create your models here.
class Clinic(models.Model):
    clinic_ID = models.IntegerField(primary_key=True,blank=False)
    clinic_name = models.CharField(max_length=100,null=False,blank=False)

class Doctor(models.Model):
    Doctor_ID = models.IntegerField(primary_key=True,blank=False)
    first_name= models.CharField(max_length=20, blank=False , null = False)
    last_name= models.CharField(max_length=20, blank=False , null = False)
    phone = models.IntegerField(max_length= 8 ,null=False, blank=False, unique=True)
    mail= models.EmailField(max_length=30,blank=False , null = False)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Patient(models.Model):
    Patient_ID = models.IntegerField(primary_key=True , blank = False)
    first_name= models.CharField(max_length=20,blank=False , null = False)
    last_name= models.CharField(max_length=20, blank=False , null = False)
    phone = models.IntegerField(max_length=8,null=False, blank=False, unique=True)
    mail= models.EmailField(max_length=30 ,blank=False , null = False)
    insurance= models.CharField(max_length=10, null=False)
    
    def __str__(self):
        return self.first_name+" "+self.last_name

class Receptionist(models.Model):
    Receptionist_ID = models.IntegerField(primary_key=True,null=False)
    clinic= models.ForeignKey(Clinic,on_delete=models.CASCADE,null=False)
    first_name= models.CharField(max_length=20 , blank=False , null = False)
    last_name= models.CharField(max_length=20 ,blank=False , null = False)
    phone = models.IntegerField(max_length=8 ,null=False, blank=False, unique=True)
    mail= models.EmailField(max_length=30 , blank=False , null = False)
    
    def __str__(self):
        return self.first_name+" "+self.last_name

class Appointmemt(models.Model):
    appointment_ID = models.IntegerField(primary_key=True,blank=False)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE,null=False)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE,null=False)
    clinic= models.ForeignKey(Clinic,on_delete=models.CASCADE,null=False)
    receptionist= models.ForeignKey(Receptionist,on_delete=models.CASCADE,null=False)
    DateTime= models.DateTimeField(null=False,blank=False , null= False)
    Duration= models.IntegerField(null=False,blank=False , null = False)
   
class ClinicManager(models.Model):
    ClinicManager_ID = models.IntegerField(primary_key=True , blank = False)
    clinic= models.ForeignKey(Clinic,on_delete=models.CASCADE , null=False)
    first_name= models.CharField(max_length=20 , blank=False , null = False)
    last_name= models.CharField(max_length=20, blank=False , null = False)
    phone = models.IntegerField(max_length=8 ,null=False, blank=False, unique=True , null=False)
    mail= models.EmailField(max_length=30 , null = False , blank = False)
    
    def __str__(self):
        return self.first_name+" "+self.last_name
    
class Room(models.Model):
    Room_ID = models.IntegerField(primary_key=True ,blank=False)
    clinic= models.ForeignKey(Clinic,on_delete=models.CASCADE,null=False)
    Title= models.CharField(max_length=100, null=False, blank=False)

class Operation(models.Model):
    operation_ID = models.IntegerField(primary_key=True , blank = False)
    Title= models.CharField(max_length=100, null=False, blank=False)

class Visit(models.Model):
    Visit_ID=models.IntegerField(primary_key=True ,blank=False)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE,null=False)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE,null=False)
    room=models.ForeignKey(Room, on_delete=models.CASCADE,null=False)
    DateTime= models.DateTimeField(null=False,blank=False , null= False)
    
    Comments= models.CharField(max_length=512,  null = True)

class Visit_Operation(models.Model):
    visitOperation_ID = models.IntegerField(primary_key=True , blank = False)
    visit= models.ForeignKey(Visit,on_delete=models.CASCADE , null=False)
    operation= models.ForeignKey(Operation,on_delete=models.CASCADE , null=False)