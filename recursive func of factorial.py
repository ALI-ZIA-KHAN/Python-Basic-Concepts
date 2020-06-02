def fact(x):
    if(x==1 or x==0):
        return 1
    else:
        return x*fact(x-1)

for x in range(0,11):
        print("the factorial of",x,"is",fact(x))
