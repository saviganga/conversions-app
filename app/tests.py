from django.test import TestCase
from django.test import Client
from django.urls import reverse
from . import views

# Create your tests here.
class TemperatureTestCase(TestCase):

    # create a client for making requests
    def setup(self):
        self.client = Client()

    # tests for index view
    def test_index_view(self):
        url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    # tests for CelciustoFahrenheit view
    def test_celciusTOfahrenheit_view(self):
        url = reverse('c-to-f')
        resp = self.client.get(url, {'c_value': 100})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 212)

    # tests for fahrenheitTOcelcius view
    def test_fahrenheitTOcelcius_view(self):
        url = reverse('f-to-c')
        resp = self.client.get(url, {'f_value': 212})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 100)