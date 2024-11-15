# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display the calculator menu
def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main code to run the calculator
def calculator():
    while True:
        display_menu()
        
        # Take user input for operation
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator.\nGoodbye!")
            break
        
        # Input numbers for the operation
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
        
        # Perform the operation based on user's choice
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}\n")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}\n")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}\n")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}\n")
        else:
            print("Invalid input! Please select a valid option (1/2/3/4/5).\n")

# Run the calculator
calculator()
