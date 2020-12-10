# vd6.py
# Mua hàng trả góp
# P : giá sản phẩm
# M: số tiền trả ban đầu
# p: lãi suất (%/năm)
# m: số tiền trả thêm mỗi tháng
# In ra: Số tiền còn lại phải trả sau 1 năm
# Nếu số tiền về  0 thì dừng lại

#VD : P = 25, M = 5, p = 7%, m = 2
P = 25
M = 5
p = 7.0
m = 2

R = P - M                   # số tiền còn lại phải trả
for thang in range(1, 12):
    tienlai = R * p/12/100
    R += tienlai - m
    if R < 0:
        break
    print(f'Số tiền sau tháng thứ {thang} là {round(R,1)} triệu')
    
