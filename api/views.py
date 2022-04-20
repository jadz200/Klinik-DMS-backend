from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers import *
from .models import *
from django.http import HttpRequest, QueryDict
from account.views import RegistrationAPIView


# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "This ":"is the base"
    }
    return Response(api_urls)


#Patient VIEWS
class patientCreateList(APIView):
    
    def get(self,request):
        if(str(request.user.roleID) != "Secretary" ):
            return Response({'message':"You are not allowed"},status.HTTP_401_UNAUTHORIZED)
        else:
            queryset = Patient.objects.all()
            serializer_class = PatientSerializer(queryset, many=True)
            return Response(serializer_class.data)
    def post(self, request, format=None):
        if(str(request.user.roleID) != "Secretary"):
            return Response({'message':"You are not allowed"},status.HTTP_401_UNAUTHORIZED)
        else:
            data=request.data
            serializer = PatientSerializer(data=request.data)
            request.data["created_by"]=str(request.user)        
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class patientRetrieveUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if(str(request.user.roleID) != "Secretary"):
            return Response({'message':"You are not allowed"},status.HTTP_401_UNAUTHORIZED)
        else:
            patient = self.get_object(pk)
            serializer = PatientSerializer(patient)
            return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        if(str(request.user.roleID) != "Secretary"):
            return Response({'message':"You are not allowed"},status.HTTP_401_UNAUTHORIZED)
        else:
            patient = self.get_object(pk)
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if(str(request.user.roleID) != "Secretary"):
            return Response({'message':"You are not allowed"},status.HTTP_401_UNAUTHORIZED)
        else:
            patient = self.get_object(pk)
            patient.delete()
            return Response({'message':"Patient Deleted"},status=status.HTTP_204_NO_CONTENT)

    
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