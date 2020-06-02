from math import *
def main():
 trig=(input("What do you want to calculate sine,cosine or tangent?"))
 if (trig=="sine"):
    a=eval(input("What is the angle measure"))
    result = sin(radians(a))
    print("The answer is" +" "+ str(round(result,3)))

 elif (trig == "cosine"):
    a = eval(input("What is the angle measure"))
    result =cos(radians(a))
    print("The answer is" + str(round(result, 3)))
 elif (trig == "tangent"):
    a = eval(input("What is the angle measure"))
    result = tan(radians(a))
    print("The answer is" + str(round(result, 3)))
 else:
    print("I DONOT UNDERSTAND")
main()