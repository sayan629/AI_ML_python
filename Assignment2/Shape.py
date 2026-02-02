#Q4. Create a class Shape with a method area().
# Create subclasses Circle , Rectangle and Triangle that override the area()method.

class Shape:
    def area(self):
        print("Area is not defined")
    
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area:",3.14*self.r*self.r) #Area of Circle= PI*r*r

class Rectangle(Shape):
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area(self):
        print("Area:",self.w,self.l)  #Area of Rectangle= width * length

class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        print("Area: ",(self.b * self.h)/2)  #Area of Triangle= (breadth * height)/2

c=Circle(5)
c.area()
r=Rectangle(4,6)
r.area()
t=Triangle(10,5)
t.area()