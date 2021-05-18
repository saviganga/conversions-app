from django.test import TestCase
from django.test import Client
from . import views

# Create your tests here.
class TemperatureTestCase(TestCase):

    # create a client for making requests
    def setup(self):
        self.client = Client()

    # tests for index view
    def test_index_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    # tests for CelciustoFahrenheit view
    def test_celciusTOfahrenheit_view(self):
        resp = self.client.get('/temp/', {'c_value': 100})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 212)
