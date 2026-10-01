from pathlib import Path


# ==========================================
# File path
# ==========================================

base_dir = Path(__file__).parent
inventory_file = base_dir / "inventory.txt"


# Activity 1
def get_valid_input():

    while True:
        stock = input("Enter stock quantity or type quit: ")
      
        if stock.lower() == "quit":
            return "quit"

        if not stock.isdigit():
            print("Invalid input")
            return none

        stock = int(stock)

        return stock 

#Activity 2
def process_delivery(current_total, new_value):

    new_total = current_total + new_value

    return new_total

#Activity 3
def calculate_tax(amount):

    tax = amount * 0.10

    return tax

#Activit 4
def generate_report(total_units, failed_attempts):

    print("===================================")
    print("Inventory Audit Report")
    print("===================================")

    print("Total Inventory:", total_units)

    print("Failed/Rejected Entries:", failed_attempts)


# Activity 5
def load_inventory():

    try:
        file = open(
            inventory_file,
            "r"
        )

        lines = file.readlines()

        file.close()


        # File exists but is empty
        if len(lines) == 0:
            return 0, []


        inventory = int(
            lines[0].strip()
        )

        history = []

        if len(lines) > 1:

            saved_history = (
                lines[1].strip()
            )

            if saved_history != "":

                values = (
                    saved_history.split(",")
                )

                for value in values:
                    history.append(
                        int(value)
                    )

        return inventory, history

    except FileNotFoundError:

        return 0, []

# Activity 6
def save_inventory(
    inventory,
    history
):

    file = open(
        inventory_file,
        "w"
    )

    file.write(
        str(inventory)
    )

    file.write("\n")

    for i in range(
        len(history)
    ):

        file.write(
            str(history[i])
        )

        if i < len(history) - 1:
            file.write(",")

    file.close()


# ==========================================
# Main Program
# ==========================================

inventory, transaction_history = (
    load_inventory()
)

failed_attempts = 0


print(
    "Previous Inventory:",
    inventory
)

print(
    "Transaction History:",
    transaction_history
)


while True:

    stock = get_valid_input()


    # If user types quit
    if stock == "quit":

        generate_report(
            inventory,
            failed_attempts
        )

        save_inventory(
            inventory,
            transaction_history
        )

        print(
            "Inventory saved."
        )

        break


    if stock is None:
        failed_attempts += 1
        
        continue


    transaction_history.append(
        stock
    )


    inventory = process_delivery(
        inventory,
        stock
    )


    tax = calculate_tax(stock)
    
    print("Current Inventory:", inventory)
    print("Tax for this delivery:", tax)

    if inventory > 500:
        print("OVERSTOCK ALERT!")

        print(
            "OVERSTOCK ALERT!"
        )