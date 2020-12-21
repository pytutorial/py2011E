#vd7
student = {
    'studentNumber': '10001',
    'name': 'Nguyen Van A',
    'email': 'nva@sch.edu'
}  #NOSQL

studentList = [
     {'studentNumber': '10001', 'name': 'Nguyen Van A', 'email': 'nva@sch.edu'},
     {'studentNumber': '10002', 'name': 'Nguyen Van B', 'email': 'nvb@sch.edu'},
     {'studentNumber': '10003', 'name': 'Nguyen Van C', 'email': 'nvc@sch.edu'},
]

#print(student['name'])
for st in studentList:
    print(st['name'])

# Yeu cau: Nhập vào mã học sinh --> in ra tên & email của học sinh đó    
code = input('Mã học sinh:')
table = {}
for st in studentList:
    key = st['studentNumber']
    value = st
    table[key] = value

student = table.get(code)
if student != None:
    print(student['name'], student['email'])
else:
    print('Mã ko tồn tại')
