#vd6.py
# In ra noi dung cua 1 file text
filename = 'vd5.py'

f = open(filename, encoding='utf-8')

#Cach1:
#text = f.read()
#print(text)

#Cach2:
#for line in f: print(line.strip())

#Cach3:
lines = f.readlines()
for line in lines: print(line.strip())

f.close()


