# vd2.py
# Nhập vào 3 số a, b, c
# TODO : In ra số nằm giữa

a = float(input('Số thứ nhất:'))
b = float(input('Số thứ hai:'))
c = float(input('Số thứ ba:'))

if (c <= a <= b) or (b <= a <= c):
    print('Số nằm giữa là :', a)

if (a <= b <= c) or (c <= b <= a):
    print('Số nằm giữa là :', b)

if (a <= c <= b) or (a <= c <= b):
    print('Số nằm giữa là :', c)
