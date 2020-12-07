#vd3
# Nhập vào 3 số
# TODO : Kiểm tra 3 số có phải 3 cạnh 1 tam giác ?

a = float(input('Số thứ nhất:'))
b = float(input('Số thứ hai:'))
c = float(input('Số thứ ba:'))

#TODO
if (a + b > c) and (b + c > a) and (c + a > b):
    print('Tam giác')
else:
    print('Không phải tam giác')
