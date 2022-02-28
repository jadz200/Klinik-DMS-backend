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
    

    path('role/',views.roleList, name="role-list") ,
    path('role/<str:pk>/',views.roleDetail, name="role-detail") ,
    path('role-create/',views.roleCreate, name="role-create") ,
    path('<str:pk>/role-update/',views.roleUpdate, name="role-update") ,
    path('<str:pk>/role-delete/',views.roleDelete, name="role-delete") ,



]
 