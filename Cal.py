num1  = int(input("Enter Number1:\t"))
num2  = int(input("Enter Number2: \t"))
operator : str = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1+num2
elif operator == '-':
    result = num1-num2
elif operator == '*':
    result = num1*num2
elif operator == '/':
    if num1 == 0 or num2 == 0:
        print("Division by Zero")
    else:
        result = num1/num2
   
else:
    print("Invalid Operator")
print("Result:",result)

    
     
