#vd4.py
# Cho 1 dãy số (có thể trùng nhau)
# Tạo ra dãy mới chỉ chứa các phần tử phân biệt
lst = [1, 2, 3, 1, 4, 5, 2, 7] # --> [1, 2, 3, 4, 5, 7]
lst_new = []

for x in lst:
    if x not in lst_new:
        lst_new.append(x)

print(lst_new)        
