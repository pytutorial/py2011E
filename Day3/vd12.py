# vd12
# Cho số N > 0
# Tìm số K nhỏ nhất 1 + 2 + .. + K > N

N = 10
S = 0
K = 1

while S + K <= N:
    S += K
    K += 1

print(K)    
