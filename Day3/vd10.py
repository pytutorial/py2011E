# vd10.py
# Ví dụ về continue
# Cho 1 dãy số
# In ra các số chia 3 dư 1 , chia 4 dư 2
ds = [1, 4, 6, 10, 14, 17, 22, 30]

for x in ds:
    if x % 3 != 1:
        continue
    
    if x % 4 != 2:
        continue

    print(x)
