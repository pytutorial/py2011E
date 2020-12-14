# vd5.py
# Nhập vào ngày giờ theo định dạng dd/mm/yyyy HH:MM:SS (24 giờ)
# Chuyển sang dạng dd/mm/yyyy HH:MM:SS AM/PM (12 giờ)
# VD : 14/12/2020 20:29:30  --> 14/12/2020 08:29:30 PM
#      14/12/2020 12:29:30  --> 14/12/2020 12:29:30 PM
st = input('Ngày giờ:')
items = st.split()
date = items[0]
time = items[1]
#print('date=', date)
#print('time=', time)
items = date.split('/')
dd = items[0]
mm = items[1]
yyyy = items[2]
            
items = time.split(':')
HH = items[0]
MM = items[1]
SS = items[2]

HH = int(HH)
AP = 'AM' if HH < 12 else 'PM'
if HH > 12: HH -= 12
print(f'{dd}/{mm}/{yyyy} {HH:02d}:{MM}:{SS} {AP}')
