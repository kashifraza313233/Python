num1  = int(input("Enter Number1:\t"))
num2  = int(input("Enter Number2: \t"))
operator : str = input("Enter an operator (+, -, *, /): ")

while operator!=0:
    if operator == '+':
        result = num1+num2
        print(f"{num1} + {num2} = {result}")
        break
    elif operator == '-':
        result = num1-num2
        print(f"{num1} - {num2} = {result}")
        break
    elif operator == '*':
        result = num1*num2
        print(f"{num1} * {num2} = {result}")
        break
    elif operator == '/':
       if num1 == 0 or num2 == 0:
           print("Division by Zero")
           break
       else:
           result = num1/num2
           print(f"{num1} / {num2} = {result}")
           break
    else:
        print("Invalid Operator")
        break

    
     
