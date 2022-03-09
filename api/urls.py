from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('',views.apiOverview, name="api-overview") ,
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('patient/',views.patientCreateList.as_view(), name="patient-list") ,
    path('patient/<str:pk>/',views.patientRetrieveUpdateDelete.as_view(), name="patient-detail") ,
    path('patient/create/',views.patientCreateList.as_view(), name="patient-create") ,
    path('patient/<str:pk>/update/',views.patientRetrieveUpdateDelete.as_view(), name="patient-update") ,
    path('patient/<str:pk>/delete/',views.patientRetrieveUpdateDelete.as_view(), name="patient-delete") ,
    

    path('role/',views.roleList, name="role-list") ,
    path('role/<str:pk>/',views.roleDetail, name="role-detail") ,
    path('role-create/',views.roleCreate, name="role-create") ,
    path('<str:pk>/role-update/',views.roleUpdate, name="role-update") ,
    path('<str:pk>/role-delete/',views.roleDelete, name="role-delete") ,

    path('clinic/',views.clinicList, name="clinic-list") ,
    path('clinic/<str:pk>/',views.clinicDetail, name="clinic-detail") ,
    path('clinic/create/',views.clinicCreate, name="clinic-create") ,
    path('clinic/<str:pk>/update/',views.clinicUpdate, name="clinic-update") ,
    path('clinic/<str:pk>/delete/',views.clinicDelete, name="clinic-delete") ,
    
    path('user/',views.userList, name="user-list") ,
    path('user/<str:pk>/',views.userDetail, name="user-detail") ,
    path('user/create/',views.userCreate, name="user-create") ,
    path('user/<str:pk>/update/',views.userUpdate, name="user-update") ,
    path('user/<str:pk>/delete/',views.userDelete, name="user-delete") ,
    
    path('room/',views.roomList, name="room-list") ,
    path('room/<str:pk>/',views.roomDetail, name="room-detail") ,
    path('room/create/',views.roomCreate, name="room-create") ,
    path('room/<str:pk>/update/',views.roomUpdate, name="room-update") ,
    path('room/<str:pk>/delete/',views.roomDelete, name="room-delete") ,
    
    path('appointment/',views.appointmentList, name="appointment-list") ,
    path('appointment/<str:pk>/',views.appointmentDetail, name="appointment-detail") ,
    path('appointment/create/',views.appointmentCreate, name="appointment-create") ,
    path('appointement/<str:pk>/update/',views.appointmentUpdate, name="appointment-update") ,
    path('appointement/<str:pk>/delete/',views.appointmentDelete, name="appointment-delete") ,

    path('journalEntryType/',views.journalEntryTypeList, name="journalEntryType-list") ,
    path('journalEntryType/<str:pk>/',views.journalEntryTypeDetail, name="journalEntryType-detail") ,
    path('journalEntryType/create/',views.journalEntryTypeCreate, name="journalEntryType-create") ,
    path('journalEntryType/<str:pk>/update/',views.journalEntryTypeUpdate, name="journalEntryType-update") ,
    path('journalEntryType/<str:pk>/delete/',views.journalEntryTypeDelete, name="journalEntryType-delete") ,

    path('paymentJournal/',views.paymentJournalList, name="paymentJournal-list") ,
    path('paymentJournal/<str:pk>/',views.paymentJournalDetail, name="paymentJournal-detail") ,
    path('paymentJournal/create/',views.paymentJournalCreate, name="paymentJournal-create") ,
    path('paymentJournal/<str:pk>/update/',views.paymentJournalUpdate, name="paymentJournal-update") ,
    path('paymentJournal/<str:pk>/delete/',views.paymentJournalDelete, name="paymentJournal-delete") ,
    
    path('visit/',views.visitList, name="visit-list") ,
    path('visit/<str:pk>/',views.visitDetail, name="visit-detail") ,
    path('visit/create/',views.visitCreate, name="visit-create") ,
    path('visit/<str:pk>/update/',views.visitUpdate, name="visit-update") ,
    path('visit/<str:pk>/delete/',views.visitDelete, name="visit-delete") ,
    
    path('operation/',views.operationList, name="operation-list") ,
    path('operation/<str:pk>/',views.operationDetail, name="operation-detail") ,
    path('operation/create/',views.operationCreate, name="operation-create") ,
    path('operation/<str:pk>/update/',views.operationUpdate, name="operation-update") ,
    path('operation/<str:pk>/delete/',views.operationDelete, name="operation-delete") ,
    
    path('visitOperation/',views.visitOperationList, name="visitOperation-list") ,
    path('visitOperation/<str:pk>/',views.visitOperationDetail, name="visitOperation-detail") ,
    path('visitOperation/create/',views.visitOperationCreate, name="visitOperation-create") ,
    path('visitOperation/<str:pk>/update/',views.visitOperationUpdate, name="visitOperation-update") ,
    path('visitOperation/<str:pk>/delete/',views.visitOperationDelete, name="visitOperation-delete") ,
]
urlpatterns = format_suffix_patterns(urlpatterns)