from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.

#Patient VIEWS


@api_view(['GET'])
def apiOverview(request): #returns all the working urls with their format
    api_urls = {
        'Patient List': '/api/patient',
        'Patient Detailed view': '/api/patient/<str:pk>',
        'Patient Create': '/api/patient-create',
        'Patient Update': '/api/<str:pk>/patient-update',
        'Patient Delete': '/api/<str:pk>/patient-delete',
        'Role List': '/api/role',
        'Role Detailed view': '/api/role/<str:pk>',
        'Role Create': '/api/role-create/',
        'Role Update': '/api/<str:pk>/role-update',
        'Role Delete': '/api/<str:pk>/role-delete',
        'admin':"see page"
    }
    return Response(api_urls)


@api_view(['GET'])
def patientList(request):
    patient = Patient.objects.all()
    serializer = PatientSerializer(patient, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def patientDetail(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(patient, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def patientCreate(request):
    serializer = PatientSerializer(data=request.data)
    print(request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def patientUpdate(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(instance=patient, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def patientDelete(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response('Deleted')

#ROLE VIEWS

@api_view(['GET'])
def roleList(request):
    role =  Role.objects.all()
    serializer = RoleSerializer(role, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def roleDetail(request, pk):
    role = Role.objects.get(id=pk)
    serializer = RoleSerializer(role, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def roleCreate(request):
    serializer = RoleSerializer(data=request.data)
    print(request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def roleUpdate(request, pk):
    role = Role.objects.get(id=pk)
    serializer = RoleSerializer(instance=role, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def roleDelete(request, pk):
    role = Role.objects.get(id=pk)
    role.delete()
    return Response("Deleted")

