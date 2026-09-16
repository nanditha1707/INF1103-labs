#Activity 1
print("===================================")
print("Smart Inventory Auditor")
print("===================================")

inventory = 0
failed = 0

#Activity 2
while True:
    stock = input("Enter stock quantity or type quit: ")
    if stock == "quit":
       break

    #Activity 4
    if not stock.isdigit():
        print("Invalid input")
        failed += 1
        continue

    #Activity 3 
    stock = int(stock)

    #Activity 5
    if stock < 0:
        print("Negative numbers are not allowed")
        failed += 1
        continue

    #Activity 6
    inventory += stock
    print("Current Inventory:", inventory)

    #Activity 7
    if inventory > 500:
        print("OVERSTOCK ALERT!")
        break