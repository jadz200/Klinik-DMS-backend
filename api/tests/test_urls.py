from django.test import SimpleTestCase
from django.urls import reverse , resolve
from api.views import apiOverview


class TestUrls(SimpleTestCase):

    def test_api_overview_resolves(self):
        url= reverse('api-overview')
        self.assertEquals(resolve(url).func , apiOverview)