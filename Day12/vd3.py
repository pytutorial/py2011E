# Mot so ham lam viec voi file/thu muc cua os
#  os.listdir(d) : Trả về các file/thư mục con trong thư muc d
#  os.path.isfile(f): Kiểm tra f có phải là file ko
#  os.path.isdir(f): Kiểm tra f có phải là thư mục
#  os.path.join(d1, d2, d3,.. f): Nối đường dẫn
#  os.rename(f1, f2) : Đổi tên
#  os.remove(f): Xóa file

#  C:\
#       A
#          B
#             C
#                 f.txt
# os.path.join('C:\\', 'A', 'B', 'C', 'f.txt') --> C:\A\B\C\f.txt

import os

def searchPythonFile(d):
    items = sorted(os.listdir(d))
    for item in items:
        item_path = os.path.join(d, item) #d + '/' + item
        if os.path.isfile(item_path) and item.lower().endswith('.py'):
            print(item_path)
        
        if os.path.isdir(item_path):
            searchPythonFile(item_path)            

searchPythonFile('.')