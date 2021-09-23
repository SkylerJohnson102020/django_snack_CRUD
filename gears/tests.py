from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Gear

class GearsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester",
            email="test@email.com",
            password="pass",
        )
        self.gear = Gear.objects.create(
            name="fig",
            purchaser=self.user,
            description="Figs are great!"
        )

    def test_gear_list_page_status_code(self):
        url = reverse('gear_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gear_list_template(self):
        url = reverse('gear_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'gear_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_gear_list_create_item(self):
        response = self.client.get(reverse('gear_list'))
        self.assertContains(response, 'fig')

    def test_gear_detail_page_status_code(self):
        response = self.client.get(reverse("gear_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "gear_detail.html")

    def test_gear_create_view(self):
        response = self.client.post(
            reverse("gear_create"),
            {
                "name": "fig",
                "purchaser": self.user.id,
                "description": "Figs are great!",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("gear_detail", args="2"))
        self.assertContains(response, "Details about fig")

    def test_gear_update_view_redirect(self):
        response = self.client.post(
            reverse("gear_update", args="1"),
            {"name": "fig", "purchaser": self.user.id, "description": "Yum!" },
        )

        self.assertRedirects(response, reverse("gear_detail", args="1"))

    def test_gear_delete_view(self):
        response = self.client.get(reverse("gear_delete", args="1"))
        self.assertEqual(response.status_code, 200)
