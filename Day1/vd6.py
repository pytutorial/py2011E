#vd6.py
# Nhập vào họ, tên đệm và tên của một người
# In ra họ tên đầy đủ của người đó

ho = input('Họ : ')
ten_dem = input('Tên đệm: ')
ten = input('Tên : ')
ho_ten = ho + ' ' + ten_dem + ' ' + ten
ho_ten = f'{ho}-{ten_dem}-{ten}'
print(ho_ten)
