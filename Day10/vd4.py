#Giải mã base64 --> ảnh
from base64 import b64decode

#print(b64decode('AQID'))
f = open('imagebase64.txt')
b64data = f.read()
f.close()

data = b64decode(b64data)
print(len(data))

f = open('out.png', 'wb')
f.write(data)
f.close()