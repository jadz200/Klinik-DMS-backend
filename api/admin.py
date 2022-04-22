from django.contrib import admin
from django import forms
from django.contrib.auth.models import BaseUserManager
from api.models import Appointment, Clinic, JournalEntryType, Patient, PaymentJournal, Role, Room, User, Visit
from django.core.mail import send_mail
from django.conf  import settings



# Register your models here.


admin.site.register(Clinic)
admin.site.register(Role)
admin.site.register(Appointment)
admin.site.register(JournalEntryType)
admin.site.register(PaymentJournal)
admin.site.register(Visit)

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','phone','clinicID','roleID','password')
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        message="Welcome to Klinic DMS, your password is :"+self.cleaned_data['password']+"\n Hope to see you at work"
        send_mail(
            'Welcome to Klinik DMS',
            message,
            settings.EMAIL_HOST_USER ,
            [self.cleaned_data['email']],
            fail_silently=False
            )
        if commit:
            user.save()
        return user
    


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form=UserForm

    list_display =('email','first_name','last_name','roleID')

    def get_changeform_initial_data(self, request):
        return {'password':BaseUserManager().make_random_password()}
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['password']
        else:
            return []

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display =('mail','first_name','last_name','phone')

    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=('title','clinicID')
