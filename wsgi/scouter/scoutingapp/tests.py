from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.


class NoUserRedirectTests(TestCase):

    def test_redirect_on_scout(self):
        self.client.logout()
        response = self.client.get('/scoutingapp/scout/')
        self.assertRedirects(response, '/scoutingapp/userlogin/',
                             status_code=302)
