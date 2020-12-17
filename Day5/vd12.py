#vd12
# Cho 1 danh sach san pham
# Sap xep san pham theo gia tang/giam dan

productList = [
    ('IPhone 8', 10.5),
    ('IPhone 7', 7.5),
    ('IPhone X', 14.5),
    ('IPhone 12', 25),
    ('IPhone 11', 17.5),
]

sorted_list = sorted(productList, key=lambda x:x[1])
for p in sorted_list:
    print(p)
