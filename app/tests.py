from django.test import TestCase, RequestFactory
from django.test import Client
from . import views

# Create your tests here.
class TemperatureTestCase(TestCase):

    # create a client for making requests
    def setup(self):
        self.client = Client()

    # test status code for celcius to fahrenheit conversion
    def test_celciusTOfahrenheit_statuscode(self):
        resp = self.client.get('/temp/')
        self.assertEqual(resp.status_code, 200)

