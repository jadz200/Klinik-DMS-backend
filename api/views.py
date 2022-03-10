from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers import *
from .models import *
# Create your views here.

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

#Patient VIEWS
class patientCreateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    

class patientRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

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
    clinic = Clinic.objects.all()
    serializer = ClinicSerializer(clinic, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def clinicDetail(request, pk):
    clinic = Clinic.objects.get(id=pk)
    serializer = ClinicSerializer(clinic, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def clinicCreate(request):
    serializer = ClinicSerializer(data=request.data)

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
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)

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


#Room views
@api_view(['GET'])
def roomList(request):
    room = Room.objects.all()
    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def roomDetail(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def roomCreate(request):
    serializer = RoomSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def roomUpdate(request, pk):
    room = room.objects.get(id=pk)
    serializer = RoomSerializer(instance=room, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def roomDelete(request, pk):
    room = room.objects.get(id=pk)
    room.delete()
    return Response('Deleted Room')

#Appointment views
@api_view(['GET'])
def appointmentList(request):
    appointment = Appointment.objects.all()
    serializer = AppointmentSerializer(appointment, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def appointmentDetail(request, pk):
    appointment = Appointment.objects.get(id=pk)
    serializer = AppointmentSerializer(appointment, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def appointmentCreate(request):
    serializer = AppointmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def appointmentUpdate(request, pk):
    appointment = appointment.objects.get(id=pk)
    serializer = AppointmentSerializer(instance=appointment, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def appointmentDelete(request, pk):
    appointment = appointment.objects.get(id=pk)
    appointment.delete()
    return Response('Deleted Appointmemt')

#JournalEntryType views
@api_view(['GET'])
def journalEntryTypeList(request):
    journalEntryType = JournalEntryType.objects.all()
    serializer = JournalEntryTypeSerializer(journalEntryType, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def journalEntryTypeDetail(request, pk):
    journalEntryType = JournalEntryType.objects.get(id=pk)
    serializer = JournalEntryTypeSerializer(journalEntryType, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def journalEntryTypeCreate(request):
    serializer = JournalEntryTypeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def journalEntryTypeUpdate(request, pk):
    journalEntryType = journalEntryType.objects.get(id=pk)
    serializer = JournalEntryTypeSerializer(instance=journalEntryType, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def journalEntryTypeDelete(request, pk):
    journalEntryType = journalEntryType.objects.get(id=pk)
    journalEntryType.delete()
    return Response('Deleted Journal Entry Type')

#PaymentJournal views
@api_view(['GET'])
def paymentJournalList(request):
    paymentJournal = PaymentJournal.objects.all()
    serializer = PaymentJournalSerializer(paymentJournal, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def paymentJournalDetail(request, pk):
    paymentJournal = PaymentJournal.objects.get(id=pk)
    serializer = PaymentJournalSerializer(paymentJournal, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def paymentJournalCreate(request):
    serializer = PaymentJournalSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def paymentJournalUpdate(request, pk):
    paymentJournal = paymentJournal.objects.get(id=pk)
    serializer = PaymentJournalSerializer(instance=paymentJournal, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def paymentJournalDelete(request, pk):
    paymentJournal = paymentJournal.objects.get(id=pk)
    paymentJournal.delete()
    return Response('Deleted Payment Journal')



#Visit views
@api_view(['GET'])
def visitList(request):
    visit = Visit.objects.all()
    serializer = VisitSerializer(visit, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def visitDetail(request, pk):
    visit = Visit.objects.get(id=pk)
    serializer = VisitSerializer(visit, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def visitCreate(request):
    serializer = VisitSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def visitUpdate(request, pk):
    visit = visit.objects.get(id=pk)
    serializer = VisitSerializer(instance=visit, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def visitDelete(request, pk):
    visit = visit.objects.get(id=pk)
    visit.delete()
    return Response('Deleted Visit')
#Operation views
@api_view(['GET'])
def operationList(request):
    operation = Operation.objects.all()
    serializer = OperationSerializer(operation, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def operationDetail(request, pk):
    operation = Operation.objects.get(id=pk)
    serializer = OperationSerializer(operation, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def operationCreate(request):
    serializer = OperationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def operationUpdate(request, pk):
    operation = operation.objects.get(id=pk)
    serializer = OperationSerializer(instance=operation, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def operationDelete(request, pk):
    operation = operation.objects.get(id=pk)
    operation.delete()
    return Response('Deleted Operation')


#Visit_Operation views
@api_view(['GET'])
def visitOperationList(request):
    visit_Operation = Visit_Operation.objects.all()
    serializer = Visit_OperationSerializer(visit_Operation, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def visitOperationDetail(request, pk):
    visit_Operation = Visit_Operation.objects.get(id=pk)
    serializer = Visit_OperationSerializer(visit_Operation, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def visitOperationCreate(request):
    serializer = Visit_OperationSerializer(data=request.data)
    print(request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def visitOperationUpdate(request, pk):
    visit_Operation = visit_Operation.objects.get(id=pk)
    serializer = Visit_OperationSerializer(instance=visit_Operation, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def visitOperationDelete(request, pk):
    visit_Operation = visit_Operation.objects.get(id=pk)
    visit_Operation.delete()
    return Response('Deleted Visit_Operation')
