# vd14
# Mua sản phẩm trả góp
# P : giá sản phẩm
# M : số tiền trả ban đầu
# p: lãi suất (%/năm)
# m: số tiền trả mỗi tháng
# In ra : số tháng để trả hết tiền sản phẩm
P = 800
M = 300
p = 7.0
m = 10

R = P - M
thang = 0
while R > 0:
    thang += 1
    tienlai = R * p/12/100
    print('tienlai=', tienlai)
    R += tienlai - m

print(thang)    
    
    
