# cal simple intrest
p=float(input("Enter Principal\n"))
r=float(input("Enter Rate in %\n"))/100
print("1.Month\n 2.Year\n 3.Weak")
ch=int(input("Enter Your Choice for Time\n"))
if(ch==1):
    t=float(input("Enter Time"))
    t=t/12
elif(ch==2):
    t = float(input("Enter Time"))
else:
    t = float(input("Enter Time"))
    t = t / 52

sol=p*(1.0+r*t)
print(sol)