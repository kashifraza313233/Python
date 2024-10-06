n1 = int(input("Enter Number :"))
n2 = int(input("Enter Number :"))
squares : list[int]  = []
for x in range(n1, n2):
    squares.append(x**2)
print(squares)