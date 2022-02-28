from dataclasses import field
from pyexpat import model
from statistics import mode
from  rest_framework import serializers
from .models import Patient, Role

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields ='__all__'
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Role
        fields='__all__'