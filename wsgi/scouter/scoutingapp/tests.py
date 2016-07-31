from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.


class NoUserRedirect(TestCase):

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


class FormInViewTests(TestCase):

    def test_signup(self):
        self.client.logout()
        response = self.client.get('/scoutingapp/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)


    def test_login(self):
        self.client.logout()
        response = self.client.get('/scoutingapp/userlogin/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
