from django.test import TestCase
from api.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(title="Producta",price=12.50, inventory_count=50)
        Product.objects.create(title="Productb",price=70, inventory_count=0)
    def test_purchaseInStock(self):
        # purchasing a product in stock should reduce it's inventory count by 1
        a = Product.objects.get(title="Producta")
        a.purchase()
        self.assertEqual(49, a.inventory_count)
    def test_purchaseNotInStock(self):
        # purchasing a product not in stock should raise a ValueError
        b = Product.objects.get(title="Productb")
        flag = False
        try:
            b.purchase()
        except ValueError:
            flag = True
        self.assertTrue(flag)
        