from math import*

##Printing Expressions Only
##Do confirm the formulas

c=float(input("Enter temperature in centigrade"))
f=(1.8*c)+32
print("The temperature in fahrenheit","is",f)


f=float(input("Enter temperature in fahrenheit"))
c=0.55*(f-32)
print("The temperature in centigrade","is",c)


length=float(input("Enter length of rectangle"))
breadth=float(input("Enter breadth of rectangle"))
area=length*breadth
print("The area of rectangle","is",area)


r=int(input("Enter radius of sphere"))
volume=(4/3)*pi*r**3
print("the volume of sphere","is",volume)


w=10
r1=1/2
r2=1
r3=2
v1=w*r1
v2=w*r2
v3=w*r3
print("The linear velocity","is",v1,"m/s")
print("The linear velocity","is",v2,"m/s")
print("The linear velocity","is",v3,"m/s")