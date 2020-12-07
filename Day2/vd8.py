# vd8: Nhập vào 3 giá trị d,m,y
# Kiểm tra xem d/m/y có là ngày hợp lệ?

# Ví dụ 
# 29/2/2020  : ok
# 29/2/2021  : not
# 31/11/2020 : not
# 30/7/2021
# 31/8/2020
# 32/10/3000
d = int(input('Ngày:'))
m = int(input('Tháng:'))
y = int(input('Năm:')) # 2000 <= y <= 2099

dmax = 31  #1,3,5,7,8,10,12

if m == 4 or m == 6 or m == 9 or m == 11:
    dmax= 30
    
if m ==2:
    if year %4 == 0: 
        dmax = 29
    else:
        dmax = 28

print(1 <= d <= dmax and 1 <= m <= 12 and y > 0)
