import math 

class Point:
    def __init__(self , x=0 , y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self) :
        # math.sqrt หารากที่ 2
        d = math.sqrt(self.x ** 2 + self.y ** 2)
        return d
    
p = Point()
dist = f'{p.distance_from_origin():.2f}'
print(f'({p.x} , {p.y}) อยู่ห่างจากศูนย์กลางเท่ากับ {dist}')