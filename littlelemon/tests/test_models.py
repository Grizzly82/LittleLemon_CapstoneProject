
from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Pie", price=5.99, Inventory=100)
        self.assertEqual(item.__str__(), "Pie : 5.99")