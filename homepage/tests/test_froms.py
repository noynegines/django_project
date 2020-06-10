from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestForms(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.login1_url = reverse('login1')
        self.user_login = {'username': 'test', 'password': '!!Test123'}
        self.users = {'username': 'test', 'first_name': 'test', 'last_name': 'test', 'email': 'test@gmail.com',
                      'password1': '!!Test123', 'password2': '!!Test123'}
        return super().setUp()


class registerTest(TestForms):
    def test_reg(self):
        response = self.client.post(self.register_url, self.users, format='text/html')
        self.assertEqual(response.status_code, 302)


class loginTest(TestForms):
    def test_login(self):
        User.objects.create_user(**self.user_login)
        response = self.client.post(self.login_url, self.user_login, follow=True)
        self.assertTrue(response.context['user'].is_active)


class register_login_homeS_form(TestForms):
    def test_user_register_login_form(self):
        response = self.client.post(self.register_url, data=self.users, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(User.objects.filter(username='test')) > 0)

        response = self.client.post(self.login_url, data=self.user_login, follow=True)

        # self.assertTemplateUsed(response, 'home/home.html')
        self.assertTrue(response.context['user'].is_authenticated)

    def test_user_register_login_login1_form(self):
        response = self.client.post(self.register_url, data=self.users, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(User.objects.filter(username='test')) > 0)

        response = self.client.post(self.login_url, data=self.user_login, follow=True)

        self.assertTrue(response.context['user'].is_authenticated)

        response = self.client.post(self.login1_url, data=self.user_login, follow=True)
        self.assertTemplateUsed(response,'simpleuser/homeSimpleuser.html')
