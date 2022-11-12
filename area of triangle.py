h=int(input("enter hieght of triangle"))
b=int(input("enter base of triangle"))
a=h*b*(0.5) #area of triangle=(hieght*base)/2
print("Area of triangle is",a)
#Area of square=side*side
s=int(input("enter the side of the square"))
side=s**2
print("Area of square is",side)
#Area of circle
import math as M
Radius=int(input("enter radius of circle"))
x=M.pi*Radius*Radius
print("Area of circle is",x)
#Area of rectangle
length=int(input("enter length"))
breath=int(input("enter breath"))
AC=length*breath
print("area of rectangle is",AC)