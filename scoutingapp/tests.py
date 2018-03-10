from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import AnonymousUser
from scoutingapp.models import MyUser
from scoutingapp.views import scout
class ScoutPageRedirect(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()

    def test_scout_redirect(self):
        request = self.factory.get('/scoutingapp/scout')

        request.user = AnonymousUser()
        response = scout(request)
        response.client = Client()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/scoutingapp/userlogin/')

class TestUser(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()
        testuser = MyUser.objects.create_user("test@example.com", password = "example")
        testuser.save()

    def test_login(self):
        c = Client()
        result = c.login(username = "test@example.com", password = "example")
        self.assertEqual(result, True)
    def test_user_needs_email(self):
        self.assertRaises(ValueError, MyUser.objects.create_user(email = None, password="example"))
