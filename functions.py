# function Parameter

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculate(operation, x, y):
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
    while True:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        result = calculate(operation, x, y)
        print("Result:", result)

        if input("Do you want to continue (y/n)? ").lower() != "y":
            break

if __name__ == "__main__":
    main()