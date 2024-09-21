# function Parameter

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers, handling zero division."""
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculate(operation, x, y):
    """Performs the specified operation on two numbers."""
    if operation == "+":
        return add(x, y)
    elif operation == "-":
        return subtract(x, y)
    elif operation == "*":
        return multiply(x, y)
    elif operation == "/":
        return divide(x, y)
    else:
        return "Invalid operation"

def main():
    """Main function to get user input and perform calculations."""
    while True:
        print("Available operations:")
        print("+ for addition")
        print("- for subtraction")
        print("* for multiplication")
        print("/ for division")

        operation = input("Enter an operation (+, -, *, /): ")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        result = calculate(operation, x, y)
        print("Result:", result)

        if input("Do you want to continue (y/n)? ").lower() != "y":
            break

if __name__ == "__main__":
    main()