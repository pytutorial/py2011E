class Category:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def toDict(self):
        return self.__dict__

    def fromDict(d):
        return Category(code=d['code'], name=d['name'])

class Product:
    def __init__(self, category, code, name, price):
        self.category = category
        self.code = code 
        self.name = name
        self.price = price
    
    def toDict(self):
        return { 'category': self.category.toDict(), 
                    'code': self.code, 'name': self.name, 'price': self.price }

    def fromDict(d):
        return Product(category=Category.fromDict(d['category']),
                         code=d['code'], name=d['name'], price=d['price'])

category = Category('DT', 'Hàng điện tử')
product = Product(category, 'IPX', 'IPhone X', 12500000)
product2 = Product(category, 'IP11', 'IPhone 11', 17500000)

import json
product_json = json.dumps(product.toDict(), indent=4)
print(product_json)

productList = [product.toDict(), product2.toDict()]
print(json.dumps(productList))

with open('product.json') as f:
    product2 = Product.fromDict(json.load(f))
    print(product2.category.name, product2.name)