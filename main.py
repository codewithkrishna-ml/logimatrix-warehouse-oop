#PROJECT-Warehouse & Supply Chain Management System
import csv
import json

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock_quantity = int(stock_quantity)

    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Category: {self.category} | Price: ${self.price:.2f} | Stock: {self.stock_quantity}"

class Supplier:
    def __init__(self, supplier_id, name, contact_number):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_number = contact_number
        self.supplier_products = []

    def __str__(self):
        return f"Supplier ID: {self.supplier_id} | Name: {self.name} | Contact: {self.contact_number}"

class WarehouseManager:
    def __init__(self):
        self.inventory = {}
        self.suppliers = {}
        self.p_counter = 1001
        self.s_counter = 5001

    def add_supplier(self, name, contact_number):
        if name.strip() == "" or contact_number.strip() == "":
            print("Error: Supplier name and contact number cannot be empty.")
            return False
        
        s_id = f"SUP-{self.s_counter}"
        new_supplier = Supplier(s_id, name, contact_number)
        self.suppliers[s_id] = new_supplier
        print(f"Supplier registered successfully with ID: {s_id}")
        self.s_counter += 1
        return True

    def add_product(self, name, category, price, stock_quantity):
        if name.strip() == "" or category.strip() == "":
            print("Error: Product name and category fields cannot be empty.")
            return False
        
        if float(price) <= 0 or int(stock_quantity) < 0:
            print("Error: Invalid price or stock values.")
            return False

        p_id = f"PID-{self.p_counter}"
        new_product = Product(p_id, name, category, price, stock_quantity)
        self.inventory[p_id] = new_product
        print(f"Product added successfully with ID: {p_id}")
        self.p_counter += 1
        return True

    def dispatch_stock(self, product_id, quantity):
        if product_id not in self.inventory:
            print("Error: Product not found in inventory.")
            return False

        product = self.inventory[product_id]
        if quantity <= 0:
            print("Error: Dispatch quantity must be greater than zero.")
            return False

        if quantity <= product.stock_quantity:
            product.stock_quantity -= quantity
            print(f"Successfully dispatched {quantity} units of {product.name}.")
            if product.stock_quantity <= 5:
                print(f"Warning: Low stock alert for {product.name}! Remaining: {product.stock_quantity}")
            return True
        else:
            print(f"Error: Not enough stock. Available: {product.stock_quantity}")
            return False

    def restock_product(self, product_id, quantity, supplier_id):
        if product_id not in self.inventory:
            print("Error: Product not found.")
            return False
        
        if supplier_id not in self.suppliers:
            print("Error: Supplier not registered.")
            return False

        if quantity <= 0:
            print("Error: Restock quantity must be greater than zero.")
            return False

        product = self.inventory[product_id]
        supplier = self.suppliers[supplier_id]
        
        product.stock_quantity += quantity
        if product.name not in supplier.supplier_products:
            supplier.supplier_products.append(product.name)
            
        print(f"Successfully restocked {quantity} units of {product.name}.")
        return True

    def show_inventory_table(self):
        if not self.inventory:
            print("Inventory is completely empty.")
            return

        print("\n" + "-"*80)
        print(f"{'PRODUCT ID':<12} | {'PRODUCT NAME':<20} | {'CATEGORY':<15} | {'PRICE':<10} | {'STOCK':<10}")
        print("-"*80)
        for p_id, p in self.inventory.items():
            print(f"{p_id:<12} | {p.name:<20} | {p.category:<15} | ${p.price:<9.2f} | {p.stock_quantity:<10}")
        print("-"*80)

    def export_to_csv(self, filename="warehouse_data.csv"):
        if not self.inventory:
            print("No data to export.")
            return

        headers = ['ProductID', 'ProductName', 'Category', 'Price', 'Stock']
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for p in self.inventory.values():
                    writer.writerow([p.product_id, p.name, p.category, p.price, p.stock_quantity])
            print(f"Data exported to CSV file: {filename}")
        except Exception as e:
            print(f"CSV export error: {e}")

    def save_to_json(self, filename="warehouse_data.json"):
        if not self.inventory and not self.suppliers:
            print("No data to save.")
            return

        data_dump = {
            "inventory": {p_id: {"name": p.name, "category": p.category, "price": p.price, "stock": p.stock_quantity} for p_id, p in self.inventory.items()},
            "suppliers": {s_id: {"name": s.name, "contact": s.contact_number, "items": s.supplier_products} for s_id, s in self.suppliers.items()}
        }
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data_dump, file, indent=4)
            print(f"Data saved to JSON file: {filename}")
        except Exception as e:
            print(f"JSON save error: {e}")

manager = WarehouseManager()

while True:
    print("\n------------ LOGIMATRIX MAIN MENU -----------------")
    print("1. Add Product")
    print("2. Register Supplier")
    print("3. Dispatch Stock")
    print("4. Restock Product")
    print("5. View Inventory Table")
    print("6. Export to CSV")
    print("7. Save to JSON File")
    print("8. Exit")

    choice = input("Select an option (1-8): ").strip()

    if choice == "1":
        name = input("Enter Product Name: ").strip()
        category = input("Enter Category: ").strip()
        try:
            price = float(input("Enter Price: ").strip())
            stock = int(input("Enter Initial Stock: ").strip())
            manager.add_product(name, category, price, stock)
        except ValueError:
            print("Error: Price and Stock must be numerical values.")

    elif choice == "2":
        s_name = input("Enter Supplier Name: ").strip()
        s_contact = input("Enter Supplier Contact: ").strip()
        manager.add_supplier(s_name, s_contact)

    elif choice == "3":
        p_id = input("Enter Product ID to dispatch: ").strip().upper()
        try:
            qty = int(input("Enter Quantity: ").strip())
            manager.dispatch_stock(p_id, qty)
        except ValueError:
            print("Error: Quantity must be a number.")

    elif choice == "4":
        p_id = input("Enter Product ID to restock: ").strip().upper()
        s_id = input("Enter Supplier ID: ").strip().upper()
        try:
            qty = int(input("Enter Quantity: ").strip())
            manager.restock_product(p_id, qty, s_id)
        except ValueError:
            print("Error: Quantity must be a number.")

    elif choice == "5":
        manager.show_inventory_table()

    elif choice == "6":
        manager.export_to_csv()

    elif choice == "7":
        manager.save_to_json()

    elif choice == "8":
        print("Exiting LogiMatrix system. Goodbye!")
        break
    else:
        print("Invalid choice! Please select an option between 1 and 8.")
