# day 74 main Filce
class Shape:
    def __init__(self,x,y) -> None:
        self.x =x 
        self.y =y
    def area (self):
        return self.x *self.y
    
class circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        super().__init__(radius,radius)

    def  area(self):
        return 3.14 * super().area()

ans = circle(10)
print(ans.area())
