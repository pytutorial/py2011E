# vd9.py
# Chương trình dự báo thời tiết
# Cho T(độ C), w (km/h), p(atm)
# In ra : Có mưa ?

T = float(input('Nhiệt độ (C):'))
w = float(input('Tốc độ gió (km/h):'))
p = float(input('Áp suất khí quyển(atm):'))
rain = False  # default

if T >= 21:
    if w >= 3 and p > 0.87:
        rain = True    
else:
    if w >= 7 or p > 1.04:
        rain = True

print(rain)
