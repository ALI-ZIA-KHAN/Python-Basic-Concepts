##table using print staement in fuctions

from math import*
def table(no,rang):
    for i in range(1,rang+1):
        c=no*i
        print(no, "*", i , "=", c)
no=int(input("Enter table of"))
rang=int(input("Where till u want"))
table(no,rang)


##table using return statements
def table(no,rang):
   for i in range(1,rang+1):
     c=no*i
     return c

x=int(input("Enter table of"))
y=int(input("Where till u want"))
table(x,y)
for i in range(1,rang+1):
 print(x,"*", i ,"=",table(x,y))



###printing table using format method
l=int(input("Enter no for table"))
m=int(input("Enter range"))
for i in range(1,m+1):
    print(f" {l} * {i} = {l*i}")