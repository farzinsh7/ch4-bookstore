from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import UserCreationForm

User = get_user_model()


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="farzin@gmail.com", password="testpass123"
        )
        self.assertEqual(user.email, "farzin@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_verified)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_verified)


class SignUpPageTests(TestCase):
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(
            self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        new_user = User.objects.create_user(
            self.email, password="somepassword")
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].email, self.email)
