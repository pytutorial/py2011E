# vd2.py
# Nhập vào họ tên đầy đủ của một người
# In ra Họ, tên đệm, tên của người đó

ho_ten = input('Họ và tên:')
#TODO :
items = ho_ten.split()
ho = items[0]
ten = items[-1]

ten_dem = ''
for i in range(1, len(items)-1):
    ten_dem += items[i] + ' '

print('Họ: ', ho)
print('Tên đệm:', ten_dem)
print('Tên: ', ten)
