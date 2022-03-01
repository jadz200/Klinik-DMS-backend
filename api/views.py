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
        'Clinic List': '/api/clinic',
        'Clinic Detailed view': '/api/clinic/<str:pk>',
        'Clinic Create': '/api/clinic-create/',
        'Clinic Update': '/api/<str:pk>/clinic-update',
        'Clinic Delete': '/api/<str:pk>/clinic-delete',
        'User List': '/api/user',
        'User Detailed view': '/api/user/<str:pk>',
        'User Create': '/api/user-create/',
        'User Update': '/api/<str:pk>/user-update',
        'User Delete': '/api/<str:pk>/user-delete',
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
    return Response('Deleted Paatient')

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
    return Response("Deleted Role")

#Clinic Views

@api_view(['GET'])
def clinicList(request):
    clinic = clinic.objects.all()
    serializer = ClinicSerializer(clinic, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def clinicDetail(request, pk):
    clinic = clinic.objects.get(id=pk)
    serializer = ClinicSerializer(clinic, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def clinicCreate(request):
    serializer = ClinicSerializer(data=request.data)
    print(request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def clinicUpdate(request, pk):
    clinic = clinic.objects.get(id=pk)
    serializer = ClinicSerializer(instance=clinic, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def clinicDelete(request, pk):
    clinic = clinic.objects.get(id=pk)
    clinic.delete()
    return Response('Deleted Clinic')


#User views
@api_view(['GET'])
def userList(request):
    user = user.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
    user = user.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    print(request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userUpdate(request, pk):
    user = user.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def userDelete(request, pk):
    user = user.objects.get(id=pk)
    user.delete()
    return Response('Deleted User')

