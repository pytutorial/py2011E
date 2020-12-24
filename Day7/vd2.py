# vd2.py
# Viết hàm tính tổng 1 dãy số
# Input : arr (List[int]): dãy số
# Output: Tổng dãy số

def arr_sum(arr):
    s = 0
    for x in arr: s += x
    return s

print(arr_sum([1, 2, 3, 4]))
