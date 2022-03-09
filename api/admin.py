from django.contrib import admin

from api.models import Appointment, Clinic, JournalEntryType, Operation, Patient, PaymentJournal, Role, Room, User, Visit, Visit_Operation

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
admin.site.register(Operation)
admin.site.register(Visit_Operation)