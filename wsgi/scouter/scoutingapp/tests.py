from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import MyUser

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


class ItemsInViewTests(TestCase):
    fixtures = ['testdata.json']

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


    def test_viewrounds(self):
        self.client.logout()
        response = self.client.get('/scoutingapp/viewrounds/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('rounds' in response.context)
        self.assertTrue('tournaments' in response.context)
        self.assertTrue('tform' in response.context)
        self.assertTrue('matchattribform' in response.context)
        self.assertTrue('viewoptionsform' in response.context)


    def test_scout(self):
        user= MyUser.objects.create_user(email='testuser@example.com')
        user.set_password('12345')
        user.save()

        self.client.login(username='testuser@example.com', password='12345')
        response = self.client.get('/scoutingapp/scout/')
        self.assertEqual(response.status_code, 200)
