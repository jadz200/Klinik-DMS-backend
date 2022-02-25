import imp
from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview") ,
    
    path('patient/',views.patientList, name="patient-list") ,
    path('patient/<str:pk>/',views.patientDetail, name="patient-detail") ,
    path('patient-create/',views.patientCreate, name="patient-create") ,
    path('<str:pk>/patient-update/',views.patientUpdate, name="patient-update") ,
    path('<str:pk>/patient-delete/',views.patientDelete, name="patient-delete") ,
    

    #path('doctor/',views.doctorList, name="doctor-list") ,
    #path('doctor/<str:pk>/',views.doctorDetail, name="doctor-detail") ,
    #path('doctor-create/',views.doctorCreate, name="doctor-create") ,
    #path('<str:pk>/doctor-update/',views.doctorUpdate, name="doctor-update") ,
    #path('doctor-delete/<str:pk>/',views.doctorDelete, name="doctor-delete") ,



]
 