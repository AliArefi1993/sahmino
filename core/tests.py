from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Item


class ItemAPITests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.item_data = {
            "date": "2025-08-16",
            "done_by": "Ali",
            "task": "Test Task",
            "type": "Branding",
            "quantity": 5,
            "base_gvt": "10.00",
            "gvt_earned": "50.00",
        }
        self.item = Item.objects.create(**self.item_data)

    def test_list_items(self):
        url = reverse("item-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_item(self):
        url = reverse("item-list-create")
        data = self.item_data.copy()
        data["task"] = "New Task"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)

    def test_delete_item(self):
        url = reverse("item-delete", args=[self.item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Item.objects.filter(id=self.item.id).exists())

    def test_item_type_choices(self):
        url = reverse("item-type-choices")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("types", response.data)
        self.assertIn("Branding", response.data["types"])

    def test_done_by_choices(self):
        url = reverse("done-by-choices")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Ali", response.data["done_by"])

    def test_update_item_put(self):
        url = reverse("item-retrieve-update", args=[self.item.id])
        data = {
            "date": "2025-08-17",
            "done_by": "Ali",
            "task": "Updated Task",
            "type": "Branding",
            "quantity": 2,
            "base_gvt": "5.00",
            "gvt_earned": "10.00",
            "status": "Done",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.task, "Updated Task")
        self.assertEqual(self.item.status, "Done")

    def test_update_item_patch(self):
        url = reverse("item-retrieve-update", args=[self.item.id])
        data = {"quantity": 10, "gvt_earned": "100.00"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(str(self.item.gvt_earned), "100.00")

    def test_done_by_totals(self):
        Item.objects.create(
            date="2025-08-16",
            done_by="Ali",
            task="Done Task",
            type="Branding",
            status="Done",
            quantity=2,
            base_gvt="5.00",
            gvt_earned="10.00",
        )
        Item.objects.create(
            date="2025-08-16",
            done_by="Javad",
            task="Done Task 2",
            type="Sale",
            status="Done",
            quantity=3,
            base_gvt="7.00",
            gvt_earned="21.00",
        )

        url = reverse("done-by-totals")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        totals = {t["done_by"]: t["total_gvt"] for t in response.data["totals"]}
        self.assertIn("Ali", totals)
        self.assertIn("Javad", totals)
