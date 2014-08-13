class Square:
    
    def area(self):
        return self.side * self.side
    def __init__(self,side=4):
        self.side = side
sq = Square(5)
area = sq.area()

sq2 = Square()
area2 =  sq2.area()
print area, area2


