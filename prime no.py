from math import*
num=int(input("Enter your no"))
for i in range(2,num):
    if num % i ==0:
        print("not prime")
        break
else:
      print(" prime ")



