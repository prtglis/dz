a = int(input("enter first mark: "))
b = int(input("enter second mark: "))
c = int(input("enter third mark: ")) 
if a < 3:
    print("unsatisfying")
elif b < 3:
    print("unsatisfying")
elif c < 3:
    print("unsatisfying")
elif a >= 4 and b >= 4 and c >= 4:
    print("excellent")
else:
    print("good")