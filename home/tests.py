from django.test import TestCase
from .models import User
from django.urls import reverse


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(phone_number='09307191285', name='طه')

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_code_page_status_code(self):
        response = self.client.get('/register/code/')
        self.assertEqual(response.status_code, 200)

    def test_welcome_page_status_code(self):
        response = self.client.get('/register/code/welcome')
        self.assertEqual(response.status_code, 200)

    def test_user_model_str(self):
        user = self.user
        str_user = f" کاربر {user.name} با شماره تلفن {user.phone_number}درخواست رزرو نوبت دارد ."
        self.assertEqual(str(user), str_user)

    def test_reserve_user_view(self):
        response = self.client.post(reverse('register'),
                                    {'phone_number': '09307191285', 'name': 'طه'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.last().name, 'طه')

    def test_check_reserve_by_phone_number(self):
        user = User.objects.get(phone_number='09307191285')
        self.assertEqual(user.name, 'طه')
