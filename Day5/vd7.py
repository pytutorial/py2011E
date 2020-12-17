# vd7.py
# Cho 1 dãy số (phân biệt)
# Tìm ra các bộ a, b, c trong dãy thỏa mãn a+b=c
lst = [1, 3, 4, 5, 8, 11, 15]

for a in lst:
    for b in lst:
        if a >= b: continue
        c = a+b
        if c in lst:
            print(f'{a}+{b}={c}')
