a = int(input("enter first mark(1-5): "))
b = int(input("enter second mark(1-5): "))
c = int(input("enter third mark(1-5): ")) 
d = int(input("enter third mark(1-5): ")) 
if a < 3 or b < 3 or c < 3 or d < 3:
    print("you are disqualified")
elif a >= 4 and b >= 4 and c >= 4 and d >=4:
    print("you are accepted with honours")
else:
    print("you are accepted")