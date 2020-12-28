#vd3.py
# Một người mua mặt hàng vào hôm nay
# Nhập vào 1 số N : số ngày vận chuyển
# T7, CN: nghỉ làm việc
# In ra ngày dự kiến nhận hàng

# Hint : Dùng hàm d.weekday()
from datetime import date, timedelta
N = int(input('Số ngày vận chuyển :'))
d = date.today()

while N > 0:
    d += timedelta(days=1)
    if d.weekday() < 5:
        N -= 1

print(d)    

