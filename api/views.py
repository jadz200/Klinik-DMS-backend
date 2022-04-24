from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers import *
from .models import *
from django.http import HttpRequest, JsonResponse
from rest_framework.permissions import IsAuthenticated
import twilio
from twilio.rest import Client
import os
import datetime

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "This ":"is the base"
    }
    return Response(api_urls)


#Patient VIEWS
class patientCreateList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class patientRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    
#User views
class userCreateList(APIView):
    def get(self,request):
        queryset = User.objects.all()
        serializer_class = UserSerializer(queryset, many=True)
        return Response(serializer_class.data)
    

class userRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Room views
class roomCreateList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

class roomRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

#Appointment views

class appointmentCreateList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    

class appointmentRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    

#JournalEntryType views
class journalEntryTypeCreateList(generics.ListCreateAPIView):
    queryset = JournalEntryType.objects.all()
    serializer_class = JournalEntryTypeSerializer
    

class journalEntryTypeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = JournalEntryType.objects.all()
    serializer_class = JournalEntryTypeSerializer

#PaymentJournal views
class paymentJournalCreateList(generics.ListCreateAPIView):
    queryset = PaymentJournal.objects.all()
    serializer_class = PaymentJournalSerializer
    

class paymentJournalRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentJournal.objects.all()
    serializer_class = PaymentJournalSerializer


#Visit views

class visitCreateList(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    

class visitRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


#CUSTOM VIEWS

#Gets Patient ID and return all the visits linked to that Patient
class userVisits(generics.ListAPIView):
    serializer_class = VisitSerializer
    def get_queryset(self):
        patient = self.kwargs['pk']
        return    Visit.objects.filter(patientID=patient)

class SendPrivateSMSPatient(APIView):
    def post(self, request, pk, format=None):
        message=request.data['message']
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        patient=Patient.objects.get(pk=pk)
        message = client.messages \
                    .create(
                         body=message,
                         from_=os.environ['TWILIO_NUMBER'],
                         to=patient.phone
                     )
        return JsonResponse({ "sent":"success"}) 
    
class SendBroadcastSMSPatient(APIView):
    def post(self, request, format=None):
        message=request.data['message']
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        phonenumbers=list(Patient.objects.values_list('phone',flat=True))
        print(phonenumbers)
        for recipient in phonenumbers:
            if recipient:
                client.messages.create(from_=os.environ['TWILIO_NUMBER'],
                                       to=recipient,
                                       body=message
                                       )
        return JsonResponse({ "sent":"success"}) 
    
#Unused Views
#ROLE VIEWS
class roleCreateList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    

class roleRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

#Clinic Views
class clinicCreateList(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class clinicRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    
    
    
#class FilterAppointement(APIView):
#    def get(self,request):
#        start_date=datetime.now()
#    #end_date=datetime.date.today+ datetime.timedelta(days=2)
#        print(start_date)
#        return JsonResponse({ "sent":"success"}) 
#    #print(end_date)
#    #appointemnts=Appointment.objects.filter(date__day(datetime()))