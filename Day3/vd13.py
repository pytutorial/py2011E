# vd13
# Cho 1 số N
# In ra số bit cần để mã hóa N
N = 100
bits = 0
while N > 0:
    bits += 1
    N //= 2

print(bits)    
