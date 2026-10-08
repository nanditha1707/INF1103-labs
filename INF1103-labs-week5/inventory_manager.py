import json
from pathlib import Path


# ==========================================
# File path
# ==========================================

base_dir = Path(__file__).parent
inventory_file = base_dir / "inventory.json"


# Activity 1
def display_all(inventory):

    print("\nCurrent Inventory")
    print("------------------------------------------------")

    if len(inventory) == 0:
        print("No products found.")

    for product in inventory:
        print(
            "ID:", product["id"],
            "| Name:", product["name"],
            "| Price: $", product["price"],
            "| Stock:", product["stock"]
        )

    print("------------------------------------------------")


# Activity 2
def add_product(inventory):

    print("\nAdd New Product")

    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

    print("Product added successfully!")


# Activity 3
def update_stock(inventory):

    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:

        if product["id"] == product_id:

            print("\nProduct Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            new_stock = int(
                input("New Stock Quantity: ")
            )

            product["stock"] = new_stock

            print("Stock updated successfully!")

            return

    print("Product not found.")


# Activity 4
def search_product(inventory):

    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:

        if product["id"] == product_id:

            print("\nProduct Found")
            print("------------------------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price: $", product["price"])
            print("Stock:", product["stock"])
            print("------------------------------------------------")

            return

    print("Product not found.")


# Activity 5
def load_inventory():

    try:
        file = open(
            inventory_file,
            "r"
        )

        inventory = json.load(file)

        file.close()

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        return inventory

    except FileNotFoundError:

        return []


# Activity 6
def save_inventory(inventory):

    file = open(
        inventory_file,
        "w"
    )

    json.dump(
        inventory,
        file,
        indent=4
    )

    file.close()


# ==========================================
# Main Program
# ==========================================

inventory = load_inventory()


# Add starting products if inventory is empty
if len(inventory) == 0:

    inventory = [
        {
            "id": "P001",
            "name": "Laptop",
            "price": 1200.00,
            "stock": 15
        },
        {
            "id": "P002",
            "name": "Mouse",
            "price": 25.50,
            "stock": 40
        },
        {
            "id": "P003",
            "name": "Keyboard",
            "price": 45.00,
            "stock": 25
        }
    ]


while True:

    print("\n========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    option = input("\nEnter option: ")


    if option == "1":

        display_all(
            inventory
        )


    elif option == "2":

        add_product(
            inventory
        )


    elif option == "3":

        update_stock(
            inventory
        )


    elif option == "4":

        search_product(
            inventory
        )


    elif option == "5":

        print("\nSaving inventory...")

        save_inventory(
            inventory
        )

        print(
            "Inventory saved successfully to inventory.json."
        )


    elif option == "6":

        print("\nSaving inventory before exit...")

        save_inventory(
            inventory
        )

        print("Inventory saved successfully.")

        print(
            "\nThank you for using Inventory Management System."
        )

        print("Program terminated.")

        break


    else:

        print("Invalid option.")
