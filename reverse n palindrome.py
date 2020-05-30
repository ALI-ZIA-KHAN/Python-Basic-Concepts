from math import*
n=str.casefold(input("Enter to check whether palindrome or not"))
x=(n[::-1])
r=x
print("After reversal",r)
if(r==n):
    print("Yes,It is palindrome")
else:
    print("No,It is not palindrome")