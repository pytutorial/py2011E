# vd8.py
# Cho 1 danh sách
# In ra bộ 3 số liên tiếp (a,b,c) mà a+b=c

ds = [1, 4, 5, 2, 7, 10, 17, 29]

N = len(ds)
for i in range(N-2):
    a = ds[i]
    b = ds[i+1]
    c = ds[i+2]
    if a + b == c:
        print(f'{a}+{b}={c}')
