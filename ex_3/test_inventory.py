import unittest
from inventory import Product, Supplier, Inventory

class TestInventory(unittest.TestCase):

    def setUp(self):
        # Set up an inventory instance and some product and supplier instances for testing
        self.inventory = Inventory()
        self.product1 = Product("001", "Apple", 50, 0.5, "Fruit")
        self.product2 = Product("002", "Banana", 100, 0.3, "Fruit")
        self.product3 = Product("003", "Carrot", 200, 0.2, "Vegetable")
        self.supplier1 = Supplier("S001", "Supplier One", "contact@supplierone.com")
        self.supplier2 = Supplier("S002", "Supplier Two", "contact@suppliertwo.com")

    def test_add_product(self):
        # Test adding a new product
        self.assertTrue(self.inventory.add_product(self.product1))
        self.assertFalse(self.inventory.add_product(self.product1))  # Duplicate product ID

    def test_remove_product(self):
        # Test removing a product
        self.inventory.add_product(self.product1)
        self.assertTrue(self.inventory.remove_product("001"))
        self.assertFalse(self.inventory.remove_product("001"))  # Already removed

    def test_update_product_quantity(self):
        # Test updating a product's quantity
        self.inventory.add_product(self.product1)
        self.assertTrue(self.inventory.update_product_quantity("001", 75))
        self.assertEqual(self.inventory.get_product("001").quantity, 75)
        self.assertFalse(self.inventory.update_product_quantity("004", 50))  # Non-existent product

    def test_update_product_price(self):
        # Test updating a product's price
        self.inventory.add_product(self.product1)
        self.assertTrue(self.inventory.update_product_price("001", 0.6))
        self.assertEqual(self.inventory.get_product("001").price, 0.6)
        self.assertFalse(self.inventory.update_product_price("004", 0.7))  # Non-existent product

    def test_get_product(self):
        # Test retrieving a product by its ID
        self.inventory.add_product(self.product1)
        self.assertEqual(self.inventory.get_product("001"), self.product1)
        self.assertIsNone(self.inventory.get_product("004"))  # Non-existent product

    def test_search_products_by_name(self):
        # Test searching products by name
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)
        self.inventory.add_product(self.product3)
        self.assertEqual(len(self.inventory.search_products_by_name("apple")), 1)
        self.assertEqual(len(self.inventory.search_products_by_name("banana")), 1)
        self.assertEqual(len(self.inventory.search_products_by_name("carrot")), 1)
        self.assertEqual(len(self.inventory.search_products_by_name("fruit")), 0)

    def test_add_supplier(self):
        # Test adding a new supplier
        self.assertTrue(self.inventory.add_supplier(self.supplier1))
        self.assertFalse(self.inventory.add_supplier(self.supplier1))  # Duplicate supplier ID

    def test_remove_supplier(self):
        # Test removing a supplier
        self.inventory.add_supplier(self.supplier1)
        self.assertTrue(self.inventory.remove_supplier("S001"))
        self.assertFalse(self.inventory.remove_supplier("S001"))  # Already removed

    def test_record_sale(self):
        # Test recording a sale
        self.inventory.add_product(self.product1)
        self.assertTrue(self.inventory.record_sale("001", 10))
        self.assertEqual(self.inventory.get_product("001").quantity, 40)
        self.assertFalse(self.inventory.record_sale("001", 100))  # Insufficient quantity
        self.assertFalse(self.inventory.record_sale("004", 10))  # Non-existent product

    def test_generate_sales_report(self):
        # Test generating a sales report
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)
        self.inventory.record_sale("001", 10)
        self.inventory.record_sale("002", 20)
        self.inventory.record_sale("001", 5)
        report = self.inventory.generate_sales_report()
        self.assertEqual(report["001"], 15)
        self.assertEqual(report["002"], 20)

    def test_get_products_by_category(self):
        # Test retrieving products by category
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)
        self.inventory.add_product(self.product3)
        fruit_products = self.inventory.get_products_by_category("Fruit")
        vegetable_products = self.inventory.get_products_by_category("Vegetable")
        self.assertEqual(len(fruit_products), 2)
        self.assertEqual(len(vegetable_products), 1)
        self.assertIn(self.product1, fruit_products)
        self.assertIn(self.product2, fruit_products)
        self.assertIn(self.product3, vegetable_products)

if __name__ == '__main__':
    unittest.main()