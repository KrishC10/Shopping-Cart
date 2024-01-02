class Product:
    def __init__(self, name, price, category):
        # Create product attributes
        self._name = name
        self._price = price
        self._category = category

    # Classify products
    def __eq__(self, other):
         if isinstance(other, Product):
             if  ((self._name == other._name and self._price == other._price) and (self._category==other._category)):
                return True
             else:
                return False
         else:
            return False

    # Create functions for various things
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    # Implement string representation
    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep

class Inventory:
    def __init__(self):
        # Make inventory a dictionary
        self.inventory_dict = {}

# Create functions for various things
    def add_to_productInventory(self, productName, productPrice, productQuantity):
        # Add a new product to the inventory
        self.inventory_dict[productName] = {'price': productPrice, 'quantity': productQuantity}

    def add_productQuantity(self, nameProduct, addQuantity):
        # Add quantity to a specific product in inventory
        self.inventory_dict[nameProduct]['quantity'] += addQuantity

    def remove_productQuantity(self, nameProduct, removeQuantity):
        # Remove quantity from a specific product in inventory
        self.inventory_dict[nameProduct]['quantity'] -= removeQuantity

    def get_productPrice(self, nameProduct):
        # Get the price of a product
        return self.inventory_dict[nameProduct]['price']

    def get_productQuantity(self, nameProduct):
        # Get the quantity of a product
        return self.inventory_dict[nameProduct]['quantity']

    def display_Inventory(self):
        # Display inventory
        for product, info in self.inventory_dict.items():
            print(f"{product}, {info['price']}, {info['quantity']}")

# Create function to populate product
def populate_inventory(inventory):
    inventory.add_to_productInventory("Backpack", 60, 100)
    inventory.add_to_productInventory("Frying pan", 80, 200)
    inventory.add_to_productInventory("Intro to Python", 90, 1000)
    inventory.add_to_productInventory("Diamond", 10000, 20)

# Main function
def main():
    # Create an instance of the Inventory class
    my_inventory = Inventory()

    # Populate inventory using populate_inventory function
    populate_inventory(my_inventory)

    # Display inventory
    my_inventory.display_Inventory()

if __name__ == "__main__":
    main()

class ShoppingCart:
    def __init__(self, buyerName, inventory):
        # Create shopping cart attributes
        self.buyerName = buyerName
        self.cart = {}

        # Inventory link
        self.inventory = inventory

    # Create a function to add items to cart
    def add_to_cart(self, nameProduct, requestedQuantity):
        # Check if the amount of product asked is availible
        if self.inventory.get_productQuantity(nameProduct) < requestedQuantity:
            return "Can not fill the order"

        # Update cart
        if nameProduct in self.cart:
            self.cart[nameProduct] += requestedQuantity
        else:
            self.cart[nameProduct] = requestedQuantity

        # Adjust inventory
        self.inventory.remove_productQuantity(nameProduct, requestedQuantity)

        return "Filled the order"

    # function to remove items from cart
    def remove_from_cart(self, nameProduct, requestedQuantity):
        # Check if product in cart
        if nameProduct not in self.cart:
            return "Product not in the cart"

        # Check if the quantity of item asked to remove is higher than what's actully avaliable
        if self.cart[nameProduct] < requestedQuantity:
            return "The requested quantity to be removed from cart exceeds what is in the cart"

        # Remove the requested quantity from the cart
        self.cart[nameProduct] -= requestedQuantity

        # Adjust inventory
        self.inventory.add_productQuantity(nameProduct, requestedQuantity)

        return "Successful"

    # Create function to view cart
    def view_cart(self):
        # Display the contents of the shopping cart, total, and buyer name
        total = 0
        for product, quantity in self.cart.items():
            price = self.inventory.get_productPrice(product)
            total += price * quantity

        print(f" {product} {quantity}")
        print(f" Total: {total}")
        print(f" Buyer Name: {self.buyerName}")


# Create function to populate inventory
def populate_inventory(inventory):
    inventory.add_to_productInventory("Backpack", 60, 100)
    inventory.add_to_productInventory("Frying Pan", 80, 200)

# Main function
def main():
    # Create an instance of the Inventory class
    my_inventory = Inventory()

    # Populate the inventory using the populate_inventory function
    populate_inventory(my_inventory)

    # Create an instance of the ShoppingCart class
    my_cart = ShoppingCart("Jane Doe", my_inventory)

    # Add items to the cart
    my_cart.add_to_cart("Backpack", 10)
    my_cart.add_to_cart("Frying Pan", 1)

    # View cart
    my_cart.view_cart()

if __name__ == "__main__":
    main()

class ProductCatalog:
    def __init__(self):
        # Create data structures
        self.catalog = []
        self.low_prices = set()
        self.medium_prices = set()
        self.high_prices = set()

    def addProduct(self, product):
        # Add new product to catalog
        self.catalog.append(product)

    def price_category(self):
        # Place products in different price categories
        for product in self.catalog:
            price = product.get_price()

            if 0 <= price <= 99:
                self.low_prices.add(product.get_name())
            elif 100 <= price <= 499:
                self.medium_prices.add(product.get_name())
            elif price >= 500:
                self.high_prices.add(product.get_name())

        # Display information about the price categories
        print(f"Number of low price items: {len(self.low_prices)}")
        print(f"Number of medium price items: {len(self.medium_prices)}")
        print(f"Number of high price items: {len(self.high_prices)}")

    def display_catalog(self):
        # Display catalog
        for product in self.catalog:
            print(f"Product: {product.get_name()} Price: {product.get_price()} Category: {product.get_category()}")

# Create function to populate catalog
def populate_catalog(catalog, inventory):
    for product_name, product_info in inventory.items():
        category = "default_category"  # Replace with the actual category logic if needed
        product = Product(product_name, product_info['price'], category)
        catalog.addProduct(product)

# Main function
def main():
    # Create an instance of the ProductCatalog class
    my_catalog = ProductCatalog()

    # Assume the inventory is a dictionary with product names as keys and information as values
    inventory_data = {
        "Backpack": {"price": 60, "quantity": 100},
        "Frying Pan": {"price": 80, "quantity": 200},
        "Intro to Python": {"price": 90, "quantity": 1000},
        "Diamond": {"price": 10000, "quantity": 20},
    }

    # Populate catalog using populate_catalog function
    populate_catalog(my_catalog, inventory_data)

    # Display information about price categories
    my_catalog.price_category()

    # Display catalog
    my_catalog.display_catalog()

if __name__ == "__main__":
    main()

# Create function to populate inventory
def populate_inventory(filename):
    try:
        with open(filename, 'r') as file:
            inventory = Inventory()
            for line in file:
                product_data = line.strip().split(',')
                if len(product_data) == 4:
                    name, price, quantity, category = product_data
                    inventory.add_to_productInventory(name, int(price), int(quantity))
            return inventory
    except FileNotFoundError:
        print(f"Could not read file: {filename}")
        return None

# Create function to populate catalog
def populate_catalog(filename):
    try:
        with open(filename, 'r') as file:
            catalog = ProductCatalog()
            for line in file:
                product_data = line.strip().split(',')
                if len(product_data) == 4:
                    name, price, quantity, category = product_data
                    product = Product(name, int(price), category)
                    catalog.addProduct(product)
            return catalog
    except FileNotFoundError:
        print(f"Could not read file: {filename}")
        return None

def main():
    # Create an instance of the ProductCatalog class
    my_catalog = ProductCatalog()

    # Assume the inventory is a dictionary with product names as keys and information as values
    inventory_data = {
        "Backpack": {"price": 60, "quantity": 100},
        "Frying Pan": {"price": 80, "quantity": 200},
        "Intro to Python": {"price": 90, "quantity": 1000},
        "Diamond": {"price": 10000, "quantity": 20},
    }

    # Populate the catalog using the populate_catalog function
    populate_catalog(my_catalog, inventory_data)

    # Display information about price categories
    my_catalog.price_category()

    # Display the catalog
    my_catalog.display_catalog()

if __name__ == "__main__":
    main()