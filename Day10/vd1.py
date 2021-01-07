# Mã hóa / giải mã json object

class Student:
    def __init__(self, name, birthYear, address):
        self.name = name
        self.birthYear = birthYear
        self.address = address

    def fromDict(d):
        name = d['name']
        birthYear = d['birthYear']
        address = d['address']
        return Student(name, birthYear, address)

student = Student('Nguyễn Văn A', 2000, 'Hà Nội')
#student = {
#    'name': 'Nguyễn Văn',
#    'birthYear': 2000,
#    'address': 'Hà Nội'
#}
import json
#Encode
student_json = json.dumps(student.__dict__, indent=2)
print(student_json)

#Decode
f = open('student.json')
student2 = Student.fromDict(json.load(f)) # json.loads(student_json)
print(student2.name)
#print(student2['name'])
f.close()


