from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.views import login,register,profile,logout,signup,admin_page,user_fill,edit_profile

class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse('login')
       # print(resolve(url))
        self.assertEquals(resolve(url).func,login)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func,register)

    def test_profile_url(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func,profile)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func,logout)

    def test_signup_url(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func,signup)

    def test_admin_page_url(self):
        url = reverse('admin_page')
        self.assertEqual(resolve(url).func,admin_page)

    def test_user_fill_url(self):
        url = reverse('user_fill')
        self.assertEqual(resolve(url).func,user_fill)

    def test_edit_profile_url(self):
        url = reverse('edit_profile')
        self.assertEqual(resolve(url).func,edit_profile)
