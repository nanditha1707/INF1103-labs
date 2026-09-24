#Activity 1
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

    print("Total Deliveries Processed:", inventory)
    print("Failed/Rejected Entries:", failed_attempts)

inventory = 0
deliveries_processed = 0
failed_attempts = 0

while True:

    stock = get_valid_input()


    # If user types quit
    if stock == "quit":

        generate_report(
            deliveries_processed,
            failed_attempts
        )

        break


    if stock is None:
        failed_attempts += 1
        
        continue

    inventory = process_delivery(
        inventory,
        stock
    )

    deliveries_processed += 1

    tax = calculate_tax(stock)
    
    print("Current Inventory:", inventory)
    print("Tax for this delivery:", tax)

    if inventory > 500:
        print("OVERSTOCK ALERT!")

        generate_report(
            deliveries_processed,
            failed_attempts
        )
        break