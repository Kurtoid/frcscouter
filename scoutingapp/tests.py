from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import MyUser

# Create your tests here.


class NoUserRedirect(TestCase):
#     fixtures = ['fixtures.json']
    def test_redirect_on_scout(self):
        self.client.logout()
        response = self.client.get('/scoutingapp/scout/')
        self.assertRedirects(response, '/scoutingapp/userlogin/',
                             status_code=302)


class UrlRedirects(TestCase):

    def test_redirect_on_no_page(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/scoutingapp/',
                             status_code=301)
