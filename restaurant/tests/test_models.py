from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_menu_str(self):
        item = Menu.objects.create(name="Pasta", description="Delicious Italian pasta", price=12.99)
        self.assertEqual(str(item), "Pasta : 12.99")
