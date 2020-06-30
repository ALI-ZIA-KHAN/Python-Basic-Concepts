##
##default value parameter

def addition(n1=0,n2=5):
    print(n1+n2)
addition()
addition(n1=6)
addition(n2=2)
addition(n1=1,n2=4)

'''
output
5
11
2
5
'''
##also

#while defining function keep default parameter at last

#def fullname(first,last,middle="khan")