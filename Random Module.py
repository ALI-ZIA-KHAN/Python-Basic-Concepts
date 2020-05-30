from random import*
##four basic attributes of random library 


#in between in two no.s
x=uniform(0,1)
print(x)

#shuffling
l1=[10,20,30,40,50]
f=shuffle(l1)
print(l1)

#choicing
n=["ALI","SARA","ZAIN","ZARA","TALHA"]
y=choice(n)
print(y)

#selecting in particular no.s
z=sample(n,2)
print(z)
