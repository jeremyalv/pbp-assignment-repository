from django.test import TestCase, Client
from django.urls import reverse

class MyWatchListTest(TestCase):
    def setUp(self):
        self.client = Client()
    def data_html_working(self):
        response = self.client.get(reverse('mywatchlist:retrieve_html'))
        self.assertEqual(response.status_code, 200)
    def data_xml_working(self):
        response = self.client.get(reverse('mywatchlist:retrieve_xml'))
        self.assertEqual(response.status_code, 200)
    def data_json_working(self):
        response = self.client.get(reverse('mywatchlist:retrieve_json'))
        self.assertEqual(response.status_code, 200)


