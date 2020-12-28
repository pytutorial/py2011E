# vd4
# Nhập vào 1 năm (2000-2099)
# In ra ngày chủ nhật cuối cùng của năm

from datetime import date, timedelta
y = int(input('Năm:'))

d = date(y, 12, 31) # 31/12/y

while d.weekday() != 6:
    d -= timedelta(days=1)

print(d)
