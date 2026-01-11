
class Circle :
    def circle_area(self , radius):
        return 3.14 * (radius ** 2)
    
    def circle_perimeter(self , radius):
        return 2 * 3.14 * radius

class Cylinder(Circle):
    def cylinder_voulme(self , radius , height):
        v = self.circle_area(radius) * height
        return v
    
    def cyliner_surface(self , radius , height):
        s = 2 * self.circle_area(radius) + \
        self.circle_perimeter(radius) * height
        return s
    

cyl = Cylinder()
r = 10 
h = 20 
print(
    f'ทรงกระบอกมีรัศมี {r} สูง {h}' ,
    f'มีปริมาตร {cyl.cylinder_voulme(r , h)}' ,
    f'พื้นผิว {cyl.cyliner_surface(r , h)}',
    sep='\n'
)