from django.test import SimpleTestCase
from django.urls import reverse , resolve
from api.views import *



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
        

