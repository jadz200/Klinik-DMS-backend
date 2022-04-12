from dataclasses import field
from pyexpat import model
from statistics import mode
from  rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields ='__all__'
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Role
        fields='__all__'
        
class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model= Clinic
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields='__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields='__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Appointment
        fields='__all__'

class JournalEntryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= JournalEntryType
        fields='__all__'
        

class PaymentJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model= PaymentJournal
        fields='__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model= Visit
        fields='__all__'
