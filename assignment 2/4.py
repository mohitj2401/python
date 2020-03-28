# Find greatest among three no.

a=int(input("Enter 1st Number"))
b=int(input("Enter 2st Number"))
c=int(input("Enter 3st Number"))
if(a<c and b<c):
    print(str(c) + " is Greater")
elif(a<b and c<b):
    print(str(b) + " is Greater")
else:
    print(str(a) + " is Greater")