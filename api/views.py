from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializer

from .models import Patient
# Create your views here and there.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/patient/',
        'Detailed view': '/patient/<str:pk>',
        'Create': '/patients/',
        'Update': '/patients/<str:pk>',
        'Delete': '/patients/<str:pk>',
        'admin/':'shows the admin panel',
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
    return Response()
