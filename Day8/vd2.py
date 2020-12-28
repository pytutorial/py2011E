# vd2.py
# Một người mua mặt hàng vào hôm nay
# Nhập vào 1 số N : số ngày vận chuyển
# In ra ngày dự kiến nhận hàng
from datetime import date, timedelta

N = int(input('Số ngày vận chuyển :'))
d = date.today()
d += timedelta(days=N)
print(d.strftime('%d/%m/%Y'))
