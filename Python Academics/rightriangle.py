from math import*
hy=int(input("enter largest side"))
a=int(input("enter other side"))
b=int(input("enter other side"))
if hy==sqrt(a*a+b*b):
    print("right triangle")
else :
    print("not right triangle")