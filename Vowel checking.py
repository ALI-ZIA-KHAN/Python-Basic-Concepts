#vowels
#i am pakistni
s=input(str.casefold("Enter any phrase"))
y=list(s)
##i, , m, ,p,a,k,i,s,t,a,n,i
print(y)

for i in range(len(y)):
    if y[i] in ["a","e","i","o","u"]:
        print(y[i],"located at",i)

s=input(str.casefold("Enter any phrase"))
y=list(s)
for i in range(len(y)):
    if(y[i]=="a" or y[i]=="e" or y[i]=="i" or y[i]=="o" or y[i]=="u"):
      print(y[i],"located at",i )
