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

    path('clinic/',views.clinicList, name="clinic-list") ,
    path('clinic/<str:pk>/',views.clinicDetail, name="clinic-detail") ,
    path('clinic-create/',views.clinicCreate, name="clinic-create") ,
    path('<str:pk>/clinic-update/',views.clinicUpdate, name="clinic-update") ,
    path('<str:pk>/clinic-delete/',views.clinicDelete, name="clinic-delete") ,
    
    path('user/',views.userList, name="user-list") ,
    path('user/<str:pk>/',views.userDetail, name="user-detail") ,
    path('user-create/',views.userCreate, name="user-create") ,
    path('<str:pk>/user-update/',views.userUpdate, name="user-update") ,
    path('<str:pk>/user-delete/',views.userDelete, name="user-delete") ,
    
    path('room/',views.roomList, name="room-list") ,
    path('room/<str:pk>/',views.roomDetail, name="room-detail") ,
    path('room-create/',views.roomCreate, name="room-create") ,
    path('<str:pk>/room-update/',views.roomUpdate, name="room-update") ,
    path('<str:pk>/room-delete/',views.roomDelete, name="room-delete") ,
    
]
 