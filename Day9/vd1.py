# vd1.py
# Tạo đối tượng hình tròn có 3 thuộc tính : x,y,R
# Viết phương thức : tính diện tích hình tròn

class Circle:
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R

    def getArea(self):
        return 3.14159 * self.R ** 2

    def isIntersected(self, circle2):
        d2 = (self.x-circle2.x)**2 + (self.y-circle2.y)**2
        return d2 <= self.R**2 + circle2.R**2

circle = Circle(4, 5, 10)
print(circle.x, circle.y, circle.R)
print('area=', circle.getArea())

circle2 = Circle(6, 7, 5)
print(circle.isIntersected(circle2))
