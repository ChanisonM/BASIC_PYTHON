class Circle :
    pi = 3.141 #Class Attribute

    def __init__(self , radius):
        self.radius = radius # Instance Attribute

    def area(self) :
        return Circle.pi * (self.radius ** 2) # pi คือ Class Attr
    
    def perimeter(self) :
        return 2 * Circle.pi * self.radius # pi คือ Class Attr
    
c1 = Circle(10)
c2 = Circle(20)
print(c1.perimeter())
print(c1.area())
print(c2.perimeter())
print(c2.area())

Circle.pi = 3.14159
c3 = Circle(30)
print(c3.perimeter())