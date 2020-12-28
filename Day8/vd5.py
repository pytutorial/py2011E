# vd5
# Tuyến xe bus bắt đầu chạy 05:30
# Tần suất : 15 phút/chuyến
# In ra thời gian chuyến bus tiếp theo
from datetime import datetime,timedelta
t = datetime.now()
print(t)

#TODO: Tao duoc t0 = 05:30 today
t0 = datetime(t.year, t.month, t.day, 5, 30, 0)
while t0 < t:
    t0 += timedelta(minutes=15)

print(t0.strftime('%H:%M %d/%m/%Y'))

