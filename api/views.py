from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers import *
from .models import *
from django.http import HttpRequest
from account.views import RegistrationAPIView
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated

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
        
    def post(self, request, format=None):

        userrequest=HttpRequest()
        usercontext={'email':request.data["email"],'roleID':request.data["roleID"],'password':'','username':''}
        userrequest.method='POST'
        userrequest.data=usercontext
        response =RegistrationAPIView.as_view()(userrequest)
        print(response)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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

class visitCreateList(APIView):
    
    def get(self,request):
            queryset = Visit.objects.all()
            serializer_class = VisitSerializer(queryset, many=True)
            return Response(serializer_class.data)
    def post(self, request, format=None):
            data=request.data
            serializer = VisitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class visitRetrieveUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return Visit.objects.get(pk=pk)
        except Visit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            visit = self.get_object(pk)
            serializer = VisitSerializer(visit)
            return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
            patient = self.get_object(pk)
            serializer = VisitSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response({'message':"Visit Deleted"},status=status.HTTP_204_NO_CONTENT)


#CUSTOM VIEWS

#Gets Patient ID and return all the visits linked to that Patient
class userVisits(generics.ListAPIView):
    serializer_class = VisitSerializer
    def get_queryset(self):
        patient = self.kwargs['pk']
        return    Visit.objects.filter(patientID=patient)
    
    
    
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