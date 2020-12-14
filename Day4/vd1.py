# vd1.py
# Nhập vào họ , tên đệm và tên của một người
# In ra họ tên đầy đủ

ho = input('Họ:')
ten_dem = input('Tên đệm:')
ten = input('Tên:')

#TODO
#C1:
print(ho, ten_dem, ten)

#C2:
ho_ten = ho + ' ' + ten_dem + ' ' + ten
print(ho_ten)

#C3
ho_ten = f'{ho} {ten_dem} {ten}'
print(ho_ten)
