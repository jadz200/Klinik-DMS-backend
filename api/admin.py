from django.contrib import admin

from api.models import Appointment, Clinic, JournalEntryType, Patient, PaymentJournal, Role, Room, User, Visit

# Register your models here.


admin.site.register(Clinic)
admin.site.register(Role)
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Appointment)
admin.site.register(JournalEntryType)
admin.site.register(PaymentJournal)
admin.site.register(Visit)
