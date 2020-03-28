x=[3,1,2,4,8];


def diff(a,b):
    return a-b;


def add( a ):
    sum = 0
    for x in a:
        sum += x
    return sum

aad={};
l=len(x)
# print(l)
for s in range(1,l-1):
    d=diff(sum(x[:s]),sum(x[s:l]));
    aad[s]=abs(d)
drf=min(aad.values())
for s in aad:
    if(aad[s]==drf):
        print(str(x[s]) + " This is equilibrium point in the given list with diffis " + str(aad[s]))
