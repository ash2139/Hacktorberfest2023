# Function to calculate addition
def add(x, y):
    return x + y

# Function to calculate subtraction
def subtract(x, y):
    return x - y

# Function to calculate multiplication
def multiply(x, y):
    return x * y

# Function to calculate division
def divide(x, y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return x / y

# Function to calculate square root
def square_root(x):
    if x < 0:
        print("Error: Square root of a negative number is not allowed.")
        return None
    return x ** 0.5

# Function to calculate power
def power(x, y):
    return x ** y

# Main program loop
while True:
    print("Simple Scientific Calculator")
    print("---------------------------")
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Quit")
    
    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Calculator exiting. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))

        # Some operations require a second number
        if choice not in ('5', '7'):
            num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
            if result is None:
                continue
        elif choice == '5':
            result = square_root(num1)
            if result is None:
                continue
        elif choice == '6':
            result = power(num1, num2)

        print("Result:", result)
    else:
        print("Invalid choice. Please enter a valid option (1-7).")
