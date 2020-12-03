# vd2.py
# Viết chương trình nhập vào tổng & hiệu của 2 số
# Yêu cầu : In ra giá trị 2 số

#Input
tong = input('Tổng 2 số: ') # --> String
hieu = input('Hiệu 2 số :') # --> String

#Process
tong = int(tong)
hieu = int(hieu)

so_lon = (tong + hieu) / 2
so_be = (tong - hieu) / 2

#Output
print('Số lớn : ' , so_lon)
print('Số bé : ', so_be)
