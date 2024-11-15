# Define a menu with item prices
menu = {
    "Pizza": 333,
    "Maggie": 385,
    "Burger": 490,
    "Cappuccino": 455,
    "Pasta": 550,
    "Noodle": 300,
    "Momos": 333,
    "French Fries": 140,
    "Black Tea": 414,
    "Soft Drink": 500,
    "Chiken Roll": 390,
    "Manchurian": 325,
    "Chinese Bhel": 400,
    "Ch. Chilli": 405,
    "Garlic Bread": 150
}

# Function to display the menu
def display_menu():
    print("Welcome to the Cafe!")
    print("Here is our menu:")
    for item, price in menu.items():
        print(f"{item}: Rs {price:.2f}")
    print()

# Function to take an order
def take_order():
    order = {}
    while True:
        item = input("Enter the name of the item you'd like to order (or type 'done' to finish): ").title()
        if item.lower() == "done":
            break
        if item in menu:
            quantity = int(input(f"How many {item}s would you like? "))
            order[item] = order.get(item, 0) + quantity
        else:
            print("Sorry, that item is not on the menu.")
    return order

# Function to calculate the total price
def calculate_total(order):
    total = 0
    print("\nYour order summary:")
    for item, quantity in order.items():
        price = menu[item] * quantity
        print(f"{item} (x{quantity}): ${price:.2f}")
        total += price
    print(f"Total: Rs {total:.2f}\n")
    return total

# Main function to run the cafe order system
def cafe_order_system():
    display_menu()
    order = take_order()
    if order:
        calculate_total(order)
    else:
        print("You did not order anything. Thank you for visiting!")

# Run the cafe order system
cafe_order_system()
