# vd6.py
# Cho biểu thức toán học: "(a+b)*(c+(d-e/f))"
# Kiểm tra thứ tự đóng mở ngoặc có đúng không
# - Số lần mở ngoặc bằng số lần đóng ngoặc
# - Không có đóng ngoặc trước mở ngoặc : ")(a + b", "(a+b))*(c"

st = input('Biểu thức:')
count = 0
for c in st:
    if c == '(':
        count += 1
    if c == ')':
        count -= 1
    if count < 0 : break

print(count==0)    
