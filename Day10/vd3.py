#Mã hóa file -> base64
from base64 import b64encode

#print(b64encode(bytes([1, 2, 3])))
f = open('IPX.jpg', 'rb')
data = f.read()  # bytes
#print(data)
f.close()

b64data = b64encode(data)
#print(b64data)
f = open('imagebase64.txt', 'w')
f.write(b64data.decode())
f.close()
