# function Parameter

def Addition(num1, num2):
    return num1 + num2
def Subtratcion(num1 , num2):
    return num1 - num2
def Multiplication(num1 , num2):
    return num1 * num2
def Division(num1 , num2):
    if num1 == 0:
        print("Error : Can't Divivde by zero")
    return num1 / num2
def Calculate(op,num1,num2):
    
    if op == "+":
       return Addition(num1,num2)
    elif op == "-":
        return Subtratcion()
    elif operation == "*":
        return Multiplication(num1,num2)
    elif operation == "/":
        return Division(num1, num2)
    else:
        return "Invalid operation"
    
def Main():
    print("Available operations:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")       
    op = input("Enter an operation (+, -, *, /): ")
    num1  = (int(input("Enter Num1 : ")))
    num2  = (int(input("Enter Num2 : ")))
    result = Calculate(op,num1,num2)
    print(f"Result {result}")
    if input("Do you want to continue (y/n)? ").lower() != "y":
        break
if __name__ == "__main__":
    main()