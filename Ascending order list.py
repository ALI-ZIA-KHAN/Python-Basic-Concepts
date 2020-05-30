from math import*
l1=[5,98,42,11,50]
print(l1)
n=len(l1)
for i in range(0,n):
    for j in range(i+1,n):
        if(l1[i]>l1[j]):
            temp=l1[j]
            l1[j]=l1[i]
            l1[i]=temp
###now in ascending order
print(l1)
