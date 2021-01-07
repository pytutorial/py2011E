# Mã hóa / giải mã json object

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def toDict(self):
        return self.__dict__

    def fromDict(d):
        street = d['street']
        city = d['city']
        return Address(street, city)

class Student:
    def __init__(self, name, birthYear, address):
        self.name = name
        self.birthYear = birthYear
        self.address = address

    def toDict(self):
        return {
            'name': self.name,
            'birthYear': self.birthYear,
            'address': self.address.toDict()
        }

    def fromDict(d):
        name = d['name']
        birthYear = d['birthYear']
        address = Address.fromDict(d['address'])
        return Student(name, birthYear, address)

addr = Address('123 Hoàn Kiếm', 'Hà Nội')
student = Student('Nguyễn Văn A', 2000, addr)
#student = {
#    'name': 'Nguyễn Văn',
#    'birthYear': 2000,
#    'address': 'Hà Nội'
#}
import json
#Encode
student_json = json.dumps(student.toDict())#, indent=2)
print(student_json)

#Decode
f = open('student.json')
student2 = Student.fromDict(json.load(f)) # json.loads(student_json)
print(student2.name)
print(student2.address.street) #-->error
#print(student2['name'])
f.close()


