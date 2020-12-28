# vd1.py
# In ra ngày tháng năm của ngày trong tuần tới có cùng thứ với ngày hôm nay
from datetime import date, timedelta
d = date.today()
d += timedelta(days=7)
print(d.strftime('%d/%m/%Y'))
