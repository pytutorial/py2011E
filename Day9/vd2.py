# vd2.py
# Tạo đối tượng hình chữ nhật có 4 thuộc tính :
#     x1, y1, x2, y2
# Viết phương thức:
#   + Tính kich thước bề ngang (getWidth())
#   + Tính kich thước bề ngang (getHeight())
#   + Tính diện tích

class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getWidth(self):
        return self.x2-self.x1

    def getHeight(self):
        return self.y2 - self.y1

    def getArea(self):
        #return (self.x2-self.x1)*(self.y2 - self.y1)
        return self.getWidth() * self.getHeight()

    def isIntersected(self, rect2):
        #return True/False
        return True

rect = Rect(1, 2, 10, 20)
print(rect.getArea())

