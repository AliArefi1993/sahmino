
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemAPITests(APITestCase):
	def setUp(self):
		self.item_data = {
			"date": "2025-08-16",
			"done_by": "Ali",
			"task": "Test Task",
			"type": "Branding",
			"quantity": 5,
			"base_gvt": "10.00",
			"gvt_earned": "50.00"
		}
		self.item = Item.objects.create(**self.item_data)

	def test_list_items(self):
		url = reverse("item-list-create")
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(len(response.data) >= 1)

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
		self.assertTrue(isinstance(response.data["types"], list))
		self.assertIn("Branding", response.data["types"])

	def test_done_by_choices(self):
		url = reverse("done-by-choices")
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn("done_by", response.data)
		self.assertTrue(isinstance(response.data["done_by"], list))
		self.assertIn("Ali", response.data["done_by"])
