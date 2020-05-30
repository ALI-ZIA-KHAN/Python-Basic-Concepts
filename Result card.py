from math import*
n=input("Enter your name")
f=input("Enter your father name")
r=int(input("Enter your roll no."))
s1=input("Enter subject name")
m1=int(input("Enter no. in this subject"))
s2=input("Enter subject name")
m2=int(input("Enter no. in this subject"))
s3=input("Enter subject name")
m3=int(input("Enter no. in this subject"))
s4=input("Enter subject name")
m4=int(input("Enter no. in this subject"))
s5=input("Enter subject name")
m5=int(input("Enter no. in this subject"))
totalmarks=500
sum=m1+m2+m3+m4+m5
p=(sum/totalmarks)*100
if(p>=90 and p<=100):
    grade="A"
    print("STUDENT NAME:",n)
    print("FATHER NAME:",f)
    print("ROLL NO:",r)
    print(s1, m1)
    print(s2, m2)
    print(s3, m3)
    print(s4, m4)
    print(s5, m5)
    print(sum)
    print(p)
    print("Your have obtained",grade,"grade")
elif(p>=80 and p<=89):
    grade="B"
    print("STUDENT NAME:",n)
    print("FATHER NAME:",f)
    print("ROLL NO:",r)
    print(s1, m1)
    print(s2, m2)
    print(s3, m3)
    print(s4, m4)
    print(s5, m5)
    print(sum)
    print(p)
    print("Your have obtained",grade,"grade")
elif(p>=70 and p<=79):
    grade="C"
    print("STUDENT NAME:",n)
    print("FATHER NAME:",f)
    print("ROLL NO:",r)
    print(s1, m1)
    print(s2, m2)
    print(s3, m3)
    print(s4, m4)
    print(s5, m5)
    print(sum)
    print(p)
    print("Your have obtained",grade,"grade")
elif (p >= 60 and p <= 69):
    grade = "D"
    print("STUDENT NAME:",n)
    print("FATHER NAME:",f)
    print("ROLL NO:",r)
    print(s1, m1)
    print(s2, m2)
    print(s3, m3)
    print(s4, m4)
    print(s5, m5)
    print(sum)
    print(p)
    print("Your have obtained", grade, "grade")
elif (p >= 50 and p <= 59):
    grade = "E"
    print("STUDENT NAME:",n)
    print("FATHER NAME:",f)
    print("ROLL NO:",r)
    print(s1, m1)
    print(s2, m2)
    print(s3, m3)
    print(s4, m4)
    print(s5, m5)
    print(sum)
    print(p)
else:
    print("you are fail")







