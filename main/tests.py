from django.test import TestCase
from .models import Item

class ItemTestCase(TestCase):
    
    def setUp(self):
        self.item = Item.objects.create(
            id = 1,
            name = "Milk",
            amount = 20,
            description = "Fresh milk from cows",
            price = 5000,
            category = "dairy",
        )

    def test_item(self):
        item_from_databases = Item.objects.get(id = self.item.id)

        self.assertEqual(item_from_databases.name, "Milk")
        self.assertEqual(item_from_databases.amount, 20)
        self.assertEqual(item_from_databases.description, "Fresh milk from cows")
        self.assertEqual(item_from_databases.price, 5000)
        self.assertEqual(item_from_databases.category, "dairy")