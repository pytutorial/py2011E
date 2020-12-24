# vd3.py
# Viết hàm để chuyển 1 số từ hệ số 10 sang hệ số 2
# Input : x (int): hệ số 10
# Output: st (string): biểu diễn trong hệ số 2

def dec2bin(x):
    st = ''
    while x > 0:
        digit = x%2
        st = str(digit) + st
        x = x//2
    return st

def dec2bin_recursive(x):
    if x <= 1: # 1 digit
        return str(x)
    return dec2bin_recursive(x//2) + str(x%2)

for i in range(0, 100):
    print(i, dec2bin(i))

for i in range(0, 100):
    print(i, dec2bin_recursive(i))    
