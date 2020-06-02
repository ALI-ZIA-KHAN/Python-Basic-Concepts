from math import*

lum=int(input("Enter no."))
for i in range(0,lum):
    if i==4:
        break
    print(i)
## 0 1 2 3

lum=int(input("Enter no."))
for i in range(0,lum):
    if i==4:
        continue
    print(i)
## 0 1 2 3 5

