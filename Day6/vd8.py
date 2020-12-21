#vd8
# Cho danh sách sản phẩm
# Nhập vào mã --> in ra tên & giá
productList = [
    {'code':'IPX', 'name': 'IPhone X', 'price': 12.5},
    {'code':'IP11', 'name': 'IPhone 11', 'price': 17.5},
    {'code':'IP12', 'name': 'IPhone 12', 'price': 25},
]
code = input('Mã sản phẩm:')
#TODO: In ra tên & giá sản phẩm
table = {}
for p in productList : table[p['code']] = p

product = table.get(code)
if product:
    print(product['name'], product['price'])
else:
    print('Không tồn tại')
                            
