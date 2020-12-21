# vd9
# Cho danh sách đơn hàng của một cửa hàng
# In ra doanh số của mỗi loại sản phẩm
orderList = [
    {'productCode': 'IPX' , 'qty': 1},
    {'productCode': 'IP11' , 'qty': 2},
    {'productCode': 'IPX' , 'qty': 1},
    {'productCode': 'IP11' , 'qty': 1},
    {'productCode': 'IP12' , 'qty': 2},
    {'productCode': 'IP11' , 'qty': 1},
]

productList = [
    {'code': 'IPX', 'price': 11.5},
    {'code': 'IP11', 'price': 17.5},
    {'code': 'IP12', 'price': 25},
]

price_table = {}
for p in productList:
    price_table[p['code']] = p['price']

#counts = {}
revenues = {}

for order in orderList:
    code = order['productCode']
    qty = order['qty']
    price = price_table[code]
    revenues[code] = revenues.get(code,0) + price*qty

print(revenues)
