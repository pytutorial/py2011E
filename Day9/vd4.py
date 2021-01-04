#vd4
# Minh họa inheritance/overwrite
from datetime import date
class Person:
    def __init__(self, name, birthYear):
        self.name = name
        self.birthYear = birthYear

    def getAge(self):
        return date.today().year - self.birthYear
    
    def introduce(self):
        print('Tên tôi là:', self.name)
        print(f'Tôi {self.getAge()} tuổi')

    #def __str__(self): return self.name
    def __repr__(self): return self.name

class Student(Person):
    def __init__(self, name, birthYear, course):
        self.name = name
        self.birthYear = birthYear
        self.course = course

    def introduce(self):
        #print('Tên tôi là:', self.name)
        #print(f'Tôi {self.getAge()} tuổi')
        super().introduce()
        print('Tôi học lớp:', self.course)

p = Person('Nguyễn Văn A', 2000)
p.introduce()
print([p])

st = Student('Nguyễn Văn B', 2000, 'Py2011E')
print(st)
st.introduce()
