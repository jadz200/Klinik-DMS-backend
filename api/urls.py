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
    
    path('appointment/',views.appointmentList, name="appointment-list") ,
    path('appointment/<str:pk>/',views.appointmentDetail, name="appointment-detail") ,
    path('appointment-create/',views.appointmentCreate, name="appointment-create") ,
    path('<str:pk>/appointment-update/',views.appointmentUpdate, name="appointment-update") ,
    path('<str:pk>/appointment-delete/',views.appointmentDelete, name="appointment-delete") ,

    path('journalEntryType/',views.journalEntryTypeList, name="journalEntryType-list") ,
    path('journalEntryType/<str:pk>/',views.journalEntryTypeDetail, name="journalEntryType-detail") ,
    path('journalEntryType-create/',views.journalEntryTypeCreate, name="journalEntryType-create") ,
    path('<str:pk>/journalEntryType-update/',views.journalEntryTypeUpdate, name="journalEntryType-update") ,
    path('<str:pk>/journalEntryType-delete/',views.journalEntryTypeDelete, name="journalEntryType-delete") ,

    path('paymentJournal/',views.paymentJournalList, name="paymentJournal-list") ,
    path('paymentJournal/<str:pk>/',views.paymentJournalDetail, name="paymentJournal-detail") ,
    path('paymentJournal-create/',views.paymentJournalCreate, name="paymentJournal-create") ,
    path('<str:pk>/paymentJournal-update/',views.paymentJournalUpdate, name="paymentJournal-update") ,
    path('<str:pk>/paymentJournal-delete/',views.paymentJournalDelete, name="paymentJournal-delete") ,
    
    path('visit/',views.visitList, name="visit-list") ,
    path('visit/<str:pk>/',views.visitDetail, name="visit-detail") ,
    path('visit-create/',views.visitCreate, name="visit-create") ,
    path('<str:pk>/visit-update/',views.visitUpdate, name="visit-update") ,
    path('<str:pk>/visit-delete/',views.visitDelete, name="visit-delete") ,
    
    path('operation/',views.operationList, name="operation-list") ,
    path('operation/<str:pk>/',views.operationDetail, name="operation-detail") ,
    path('operation-create/',views.operationCreate, name="operation-create") ,
    path('<str:pk>/operation-update/',views.operationUpdate, name="operation-update") ,
    path('<str:pk>/operation-delete/',views.operationDelete, name="operation-delete") ,
    
    path('visitOperation/',views.visitOperationList, name="visitOperation-list") ,
    path('visitOperation/<str:pk>/',views.visitOperationDetail, name="visitOperation-detail") ,
    path('visitOperation-create/',views.visitOperationCreate, name="visitOperation-create") ,
    path('<str:pk>/visitOperation-update/',views.visitOperationUpdate, name="visitOperation-update") ,
    path('<str:pk>/visitOperation-delete/',views.visitOperationDelete, name="visitOperation-delete") ,
]
 