class Shape():
    def is_number(self , x) :
        try :
            float(x)
        except ValueError : return False
        else : return True

    def circle_area(self , radius) :
        if self.is_number(radius) and radius > 0 :
            return 3.141 * (radius ** 2)
        else : None

    def rect_area(self , width , height):
        if self.is_number(width) and \
            self.is_number(height) and \
            width > 0 and height > 0 :
            return width * height
        
        else : return None

shape = Shape()

print(shape.circle_area(10))
print(shape.rect_area(10,-20))
print(shape.rect_area(10,20))