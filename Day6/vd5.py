# vd5.py
# cho 1 dãy số
# In ra số lần xuất hiện của các số phân biệt
lst = [1, 2, 3, 1, 2, 5, 6, 7, 2, 3, 10000]
counts = {}
for x in lst:
    counts[x] = counts.get(x, 0) + 1

for x in counts:
    print(x, ':' , counts[x])
