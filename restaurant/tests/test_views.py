from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(name="Pizza", description="Cheesy", price=10.99)
        self.item2 = Menu.objects.create(name="Salad", description="Fresh", price=6.99)

    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/')  # Adjust URL if different in your project
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
