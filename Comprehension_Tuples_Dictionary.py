# List Comprehensions

n1 = int(input("Enter Number :"))
n2 = int(input("Enter Number :"))
squares : list[int]  = []
for x in range(n1, n2):
    squares.append(x**2)
print(squares)


# Simplify Code with List Comprehensions

squares : list[int] = [x**2 for x in range(1, 6)]
print(squares)  