# vd17
# chương trình tính hóa đơn nhiều mức giá
# 0-10:  6K/m3
# 10-20: 7K/m3
# 20-30: 9K/m3
# 30+ :  16K/m3
muc_so = [0, 10, 20, 30]
muc_gia = [6, 7, 9, 16]
so_nuoc = float(input('Số nước:'))

i = 0  # chi so muc gia
tong_tien = 0
while so_nuoc > 0:
    han_muc = min(10, so_nuoc)
    tong_tien += muc_gia[i] * han_muc
    so_nuoc -= han_muc
    i += 1

print(tong_tien)
