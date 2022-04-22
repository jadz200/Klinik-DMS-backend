from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('',views.apiOverview, name="api-overview") ,

    path('patient/',views.patientCreateList.as_view(), name="patient-list") ,
    path('patient/create/',views.patientCreateList.as_view(), name="patient-create") ,
    path('patient/<str:pk>/',views.patientRetrieveUpdateDelete.as_view(), name="patient-detail") ,
    path('patient/<str:pk>/update/',views.patientRetrieveUpdateDelete.as_view(), name="patient-update") ,
    path('patient/<str:pk>/delete/',views.patientRetrieveUpdateDelete.as_view(), name="patient-delete") ,
    

    path('role/',                views.roleCreateList.as_view(), name="role-list") ,
    path('role/create/',         views.roleCreateList.as_view(), name="role-create") ,
    path('role/<str:pk>/',       views.roleRetrieveUpdateDelete.as_view(), name="role-detail") ,
    path('role/<str:pk>/update/',views.roleRetrieveUpdateDelete.as_view(), name="role-update") ,
    path('role/<str:pk>/delete/',views.roleRetrieveUpdateDelete.as_view(), name="role-delete") ,

    path('clinic/',                views.clinicCreateList.as_view(), name="clinic-list") ,
    path('clinic/create/',         views.clinicCreateList.as_view(), name="clinic-create") ,
    path('clinic/<str:pk>/',       views.clinicRetrieveUpdateDelete.as_view(), name="clinic-detail") ,
    path('clinic/<str:pk>/update/',views.clinicRetrieveUpdateDelete.as_view(), name="clinic-update") ,
    path('clinic/<str:pk>/delete/',views.clinicRetrieveUpdateDelete.as_view(), name="clinic-delete") ,
    
    path('user/',                views.userCreateList.as_view(), name="user-list") ,
    path('user/create/',         views.userCreateList.as_view(), name="user-create") ,
    path('user/<str:pk>/',       views.userRetrieveUpdateDelete.as_view(), name="user-detail") ,
    path('user/<str:pk>/update/',views.userRetrieveUpdateDelete.as_view(), name="user-update") ,
    path('user/<str:pk>/delete/',views.userRetrieveUpdateDelete.as_view(), name="user-delete") ,
    
    path('room/',                views.roomCreateList.as_view(), name="room-list") ,
    path('room/create/',         views.roomCreateList.as_view(), name="room-create") ,
    path('room/<str:pk>/',       views.roomRetrieveUpdateDelete.as_view(), name="room-detail") ,
    path('room/<str:pk>/update/',views.roomRetrieveUpdateDelete.as_view(), name="room-update") ,
    path('room/<str:pk>/delete/',views.roomRetrieveUpdateDelete.as_view(), name="room-delete") ,
    
    path('appointment/',                views.appointmentCreateList.as_view(), name="appointment-list") ,
    path('appointment/create/',         views.appointmentCreateList.as_view(), name="appointment-create") ,
    path('appointment/<str:pk>/',       views.appointmentRetrieveUpdateDelete.as_view(), name="appointment-detail") ,
    path('appointment/<str:pk>/update/',views.appointmentRetrieveUpdateDelete.as_view(), name="appointment-update") ,
    path('appointment/<str:pk>/delete/',views.appointmentRetrieveUpdateDelete.as_view(), name="appointment-delete") ,

    path('journalEntryType/',                views.journalEntryTypeCreateList.as_view(), name="journalEntryType-list") ,
    path('journalEntryType/create/',         views.journalEntryTypeCreateList.as_view(), name="journalEntryType-create") ,
    path('journalEntryType/<str:pk>/',       views.journalEntryTypeRetrieveUpdateDelete.as_view(), name="journalEntryType-detail") ,
    path('journalEntryType/<str:pk>/update/',views.journalEntryTypeRetrieveUpdateDelete.as_view(), name="journalEntryType-update") ,
    path('journalEntryType/<str:pk>/delete/',views.journalEntryTypeRetrieveUpdateDelete.as_view(), name="journalEntryType-delete") ,

    path('paymentJournal/',                views.paymentJournalCreateList.as_view(), name="paymentJournal-list") ,
    path('paymentJournal/create/',         views.paymentJournalCreateList.as_view(), name="paymentJournal-create") ,
    path('paymentJournal/<str:pk>/',       views.paymentJournalRetrieveUpdateDelete.as_view(), name="paymentJournal-detail") ,
    path('paymentJournal/<str:pk>/update/',views.paymentJournalRetrieveUpdateDelete.as_view(), name="paymentJournal-update") ,
    path('paymentJournal/<str:pk>/delete/',views.paymentJournalRetrieveUpdateDelete.as_view(), name="paymentJournal-delete") ,
    
    path('visit/',                views.visitCreateList.as_view(), name="visit-list") ,
    path('visit/create/',         views.visitCreateList.as_view(), name="visit-create") ,
    path('visit/<str:pk>/',       views.visitRetrieveUpdateDelete.as_view(), name="visit-detail") ,
    path('visit/<str:pk>/update/',views.visitRetrieveUpdateDelete.as_view(), name="visit-update") ,
    path('visit/<str:pk>/delete/',views.visitRetrieveUpdateDelete.as_view(), name="visit-delete") ,
    

    path('patient/<str:pk>/visits/', views.userVisits.as_view(), name="user visits"),

    path('sms/broadcast/',views.SendBroadcastSMSPatient.as_view(),name="Send sms to 1 person"),
    path('sms/patient/<str:pk>/',views.SendPrivateSMSPatient.as_view(),name="Send sms to 1 person")


]
urlpatterns = format_suffix_patterns(urlpatterns)