# vd11
# Cho bảng dữ liệu sản phẩm
# Mỗi sản phẩm có 2 trường tên & giá
# Nhập vào khoảng giá (pmin-pmax)
# Yêu cầu : In ra các sản phẩm trong khoảng giá đó
productList = [
    ('IPhone 7', 7.5),
    ('IPhone 8', 10.5),
    ('IPhone X', 14.5),
    ('IPhone 11', 17.5),
    ('IPhone 12', 25.0),
]
pmin, pmax = (10, 15)
print([p[0] for p in productList if pmin <= p[1] <= pmax])
