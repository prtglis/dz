a = int(input("age of the car: "))
b = int(input("enter mialeage in car(km): "))
if a < 3 and  b < 30000 :
    print("car is in perfect condition")
elif a < 10 and b < 100000 :
    print("car is in good condition")
else:
    print("car pending further investigation")