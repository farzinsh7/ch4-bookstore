from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "pages/home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Homepage")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):  # new
        view = resolve("/")
        self.assertEqual(view.func.view_class, HomePageView)
