class Product:
    def __init__(self, product_id, name, quantity, price, category):
        # Constructor to initialize a product with ID, name, quantity, price, and category
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        # Constructor to initialize a supplier with ID, name, and contact information
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

class Inventory:
    def __init__(self):
        # Constructor to initialize the inventory with empty dictionaries for products and suppliers
        self.products = {}
        self.suppliers = {}
        self.sales = []

    def add_product(self, product):
        # Adds a product to the inventory if the product ID is not already present
        if product.product_id in self.products:
            return False
        self.products[product.product_id] = product
        return True

    def remove_product(self, product_id):
        # Removes a product from the inventory by its ID
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False

    def update_product_quantity(self, product_id, quantity):
        # Updates the quantity of a product in the inventory
        if product_id in self.products:
            self.products[product_id].quantity = quantity
            return True
        return False

    def update_product_price(self, product_id, price):
        # Updates the price of a product in the inventory
        if product_id in self.products:
            self.products[product_id].price = price
            return True
        return False

    def get_product(self, product_id):
        # Retrieves a product from the inventory by its ID
        return self.products.get(product_id, None)

    def search_products_by_name(self, name):
        # Searches for products in the inventory by name (case-insensitive)
        return [product for product in self.products.values() if name.lower() in product.name.lower()]

    def add_supplier(self, supplier):
        # Adds a supplier to the inventory if the supplier ID is not already present
        if supplier.supplier_id in self.suppliers:
            return False
        self.suppliers[supplier.supplier_id] = supplier
        return True

    def remove_supplier(self, supplier_id):
        # Removes a supplier from the inventory by their ID
        if supplier_id in self.suppliers:
            del self.suppliers[supplier_id]
            return True
        return False

    def record_sale(self, product_id, quantity):
        # Records a sale of a product, reducing its quantity in the inventory
        if product_id in self.products and self.products[product_id].quantity >= quantity:
            self.products[product_id].quantity -= quantity
            self.sales.append((product_id, quantity))
            return True
        return False

    def generate_sales_report(self):
        # Generates a sales report with total sales for each product
        report = {}
        for product_id, quantity in self.sales:
            if product_id in report:
                report[product_id] += quantity
            else:
                report[product_id] = quantity
        return report

    def get_products_by_category(self, category):
        # Retrieves all products in a specific category
        return [product for product in self.products.values() if product.category == category]