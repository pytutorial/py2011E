# vd10.py
# TÍnh cước taxi
# Giá mở cửa : 5000 đ/300 met đầu
# Từ 300m-2.0 km : 17400đ/1km
# Từ 2.0 km trở đi : 13100đ/1km
# Nhập vào : quãng đường (km)
# Yêu cầu : In ra số tiền

s = float(input('Quãng đường (km):'))

if s < 0.3:
    sotien = 5000
elif s < 2.0:
    sotien = 5000 + (s-0.3)*17400
else:
    sotien = 5000 + 17400 * 1.7 + (s - 2) * 13100
    
print('Số tiền :', sotien)
