class Triangle():
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def getArea(self):
        print(self.base*self.height/2,"is area of triangle")
        
class Square(Triangle):
    def __init__(self,side):
        self.side = side
        Triangle.__init__(self,side,side)
        
    def getArea(self):
        print(self.side*self.side,"is area of square")
        
        
t = Triangle(2,6)
s = Square(4)
t.getArea()
s.getArea()