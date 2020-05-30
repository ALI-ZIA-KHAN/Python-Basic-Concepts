import cmath
def quad(a,b,c):
  if(a==0):
   print("The equation cannot be solved")
  else:
   d=b**2-(4*a*c)
  s1=(-b-cmath.sqrt(d))/2*a
  s2=(-b+cmath.sqrt(d))/2*a
  return s1,s2
a1=float(input("enter value of a"))
b1=float(input("enter value of b"))
c1=float(input("enter value of c"))
s11,s12=quad(a1,b1,c1)
print("the solutions are {0},{1}".format(s11,s12))