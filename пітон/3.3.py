a = int(input("enter your age: "))
b = int(input("enter total cost of your basket: "))
if a <=18:
    b = b - (b * 0.10)
    print(f'total cost is: {b}')
elif a <=60:
    b = b - (b * 0.05)
    print(f'total cost is: {b}')
else:
    b = b - (b * 0.15)
    print(f'total cost is: {b}')