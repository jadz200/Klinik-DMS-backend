from django.test import SimpleTestCase
from django.urls import reverse , resolve
from api.views import *


class TestUrlsPatients(SimpleTestCase):
    
    def test_api_overview_resolves(self):
        url= reverse('api-overview')
        self.assertEquals(resolve(url).func , apiOverview) 
        
    def test_patient_list(self):
        url= reverse('patient-list')
        self.assertEquals(resolve(url).func , patientList) 
        
    def test_patient_detail(self):
        url= reverse('patient-detail', args=["pk"])
        self.assertEquals(resolve(url).func , patientDetail) 

    def test_patient_create(self):
        url= reverse('patient-create')
        self.assertEquals(resolve(url).func , patientCreate) 

    def test_patient_update(self):
        url= reverse('patient-update', args=["pk"])
        self.assertEquals(resolve(url).func , patientUpdate) 

    def test_patient_delete(self):
        url= reverse('patient-delete', args=["pk"])
        self.assertEquals(resolve(url).func , patientDelete) 
        
class TestUrlsRoles(SimpleTestCase):

    def test_role_list(self):
        url= reverse('role-list')
        self.assertEquals(resolve(url).func , roleList) 
        
    def test_role_detail(self):
        url= reverse('role-detail', args=["pk"])
        self.assertEquals(resolve(url).func , roleDetail) 

    def test_role_create(self):
        url= reverse('role-create')
        self.assertEquals(resolve(url).func , roleCreate) 

    def test_role_update(self):
        url= reverse('role-update', args=["pk"])
        self.assertEquals(resolve(url).func , roleUpdate) 

    def test_role_delete(self):
        url= reverse('role-delete', args=["pk"])
        self.assertEquals(resolve(url).func , roleDelete)
        

class TestUrlsClinics(SimpleTestCase):

    def test_clinic_list(self):
        url= reverse('clinic-list')
        self.assertEquals(resolve(url).func , clinicList) 
        
    def test_clinic_detail(self):
        url= reverse('clinic-detail', args=["pk"])
        self.assertEquals(resolve(url).func , clinicDetail) 

    def test_clinic_create(self):
        url= reverse('clinic-create')
        self.assertEquals(resolve(url).func , clinicCreate) 

    def test_clinic_update(self):
        url= reverse('clinic-update', args=["pk"])
        self.assertEquals(resolve(url).func , clinicUpdate) 

    def test_clinic_delete(self):
        url= reverse('clinic-delete', args=["pk"])
        self.assertEquals(resolve(url).func , clinicDelete) 


class TestUrlsUsers(SimpleTestCase):

    def test_user_list(self):
        url= reverse('user-list')
        self.assertEquals(resolve(url).func , userList) 
        
    def test_user_detail(self):
        url= reverse('user-detail', args=["pk"])
        self.assertEquals(resolve(url).func , userDetail) 

    def test_user_create(self):
        url= reverse('user-create')
        self.assertEquals(resolve(url).func , userCreate) 

    def test_user_update(self):
        url= reverse('user-update', args=["pk"])
        self.assertEquals(resolve(url).func , userUpdate) 

    def test_user_delete(self):
        url= reverse('user-delete', args=["pk"])
        self.assertEquals(resolve(url).func , userDelete)