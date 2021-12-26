from django.test import TestCase, RequestFactory
from .views import GetRedirect, CreateNewShort
from .models import Urls
import json

class TestApi(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.short_url = "1"

    def test_create_short_url_200_OK(self):
        data = {
            "long_url": "https://www.markdownguide.org/basic-syntax/",
            "limited": True
        }
        request = self.factory.post(
            '/short/create/', data, content_type='application/json')
        
        response = CreateNewShort.as_view()(request)
        self.short_url = response.get('short')


        self.assertEqual(response.status_code, 201)
    
    def test_redirect(self):
        data = {
            "long_url": "https://www.markdownguide.org/basic-syntax/",
            "limited": True
        }
        request = self.factory.post(
            '/short/create/', data, content_type='application/json')
        
        response = CreateNewShort.as_view()(request)

        data = eval(response.content.decode())

        short_url = data.get('short')
        hash = short_url.split('/')[-2]

        request = self.factory.get(
            f'{short_url}')
        response = GetRedirect.as_view()(request, hash=hash)
        self.assertEqual(response.status_code, 302)

        request = self.factory.get(
            f'{short_url}')
        
        response = GetRedirect.as_view()(request, hash=hash)
        self.assertEqual(response.status_code, 400)
