# vd3.py
# Cho danh sách các thời điểm khách hàng đến cửa hàng
# In ra các khung giờ có KH 
timestamps = ['06:45', '06:50', '07:05', '07:15', '08:05',
         '11:45', '11:50', '11:55', '12:15', '12:30', '13:05',
         '18:45', '18:50', '19:15', '19:30', '19:45'
]

#TODO : 06-07, 07-08, 08-09, 11-12, 12-13, 13-14, 18-19, 19-20
hours = set()
for timestamp in timestamps:
    hour, minute = timestamp.split(':')
    #print(hour, minute)
    hours.add(hour)

for hour in sorted(hours):
    print(f'{hour}-{int(hour)+1:02d}')
 
