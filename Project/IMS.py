class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id     = product_id
        self.name           = name
        self.category       = category
        self.price          = price
        self.stock_quantity = stock_quantity

    def update_product(self, name=None, category=None, price=None, stock_quantity=None):
        if name:
            self.name = name
        if category:
            self.category = category
        if price:
            self.price = price
        if stock_quantity is not None:
            self.stock_quantity = stock_quantity
        print(f"Product '{self.product_id}' updated successfully.")

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product ID already exists.")
        else:
            self.products[product.product_id] = product
            print(f"Product '{product.name}' added successfully.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product '{product_id}' deleted successfully.")
        else:
            print("Product ID not found.")

    def view_all_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products.values():
                self.display_product(product)

    def display_product(self, product):
        print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
              f"Price: ${product.price:.2f}, Stock: {product.stock_quantity}")

    def search_product(self, search_term):
        found = False
        for product in self.products.values():
            if search_term.lower() in product.name.lower() or search_term.lower() in product.category.lower():
                self.display_product(product)
                found = True
        if not found:
            print("No matching products found.")

    def adjust_stock(self, product_id, quantity):
        if product_id in self.products:
            product = self.products[product_id]
            product.stock_quantity += quantity
            action = "restocked" if quantity > 0 else "reduced"
            print(f"Product '{product.name}' {action} by {abs(quantity)} units.")
            if product.stock_quantity < 5:  # Low stock threshold
                print(f"Warning: Low stock for product '{product.name}'. Consider restocking.")
        else:
            print("Product ID not found.")
inventory = Inventory()

def main_menu():
    while True:
        print("\nInventory Management System")
        print("1. View All Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Adjust Stock")
        print("6. Search Product")
         
        choice = input("Choose an option: ")

        if choice == '1':
            inventory.view_all_products()
        elif choice == '2': # and role == "Admin":
            add_product()
        elif choice == '3': # and role == "Admin":
            update_product()
        elif choice == '4': # and role == "Admin":
            delete_product()
        elif choice == '5': # and role == "Admin":
            adjust_stock()
        elif choice == '6':
            search_product()
        else:
            print("Invalid choice or insufficient permissions.")
            
def add_product():
    try:
        product_id     = input("Enter Product ID: ")
        name           = input("Enter Product Name: ")
        category       = input("Enter Product Category: ")
        price          = float(input("Enter Product Price: "))
        stock_quantity = int(input("Enter Stock Quantity: "))
        product = Product(product_id, name, category, price, stock_quantity)
        inventory.add_product(product)
    except ValueError:
        print("Invalid input. Price and Stock Quantity should be numbers.")

def update_product():
    product_id = input("Enter Product ID to update: ")
    if product_id in inventory.products:
        name           = input("Enter new name (leave blank to keep current): ")
        category       = input("Enter new category (leave blank to keep current): ")
        price          = input("Enter new price (leave blank to keep current): ")
        stock_quantity = input("Enter new stock quantity (leave blank to keep current): ")

        try:
            price = float(price) if price else None
            stock_quantity = int(stock_quantity) if stock_quantity else None
            inventory.products[product_id].update_product(name, category, price, stock_quantity)
        except ValueError:
            print("Invalid input for price or stock quantity.")
    else:
        print("Product ID not found.")

def delete_product():
    product_id = input("Enter Product ID to delete: ")
    inventory.delete_product(product_id)

def adjust_stock():
    product_id = input("Enter Product ID for stock adjustment: ")
    try:
        quantity = int(input("Enter quantity to adjust Stock: "))
        inventory.adjust_stock(product_id, quantity)
    except ValueError:
        print("Invalid quantity. Must be an integer.")

def search_product():
    search_term = input("Enter product name or category to search: ")
    inventory.search_product(search_term)

if __name__ == '__main__':
    main_menu()
