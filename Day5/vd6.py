#vd6.py
# Cho 2 dãy số
# Tìm cặp phần tử x thuộc dãy 1, y thuộc dãy 2
# sao  cho |x-y| nhỏ nhất

lst1 = [1, 5, 10, 15]
lst2 = [3, 9, 12, 20]

x_min = lst1[0]
y_min = lst2[0]
d_min = abs(x_min - y_min)

for x in lst1:
    for y in lst2:
        d = abs(x-y)
        if d < d_min:
            d_min = d
            x_min = x
            y_min = y
print(x_min, y_min, d_min)            
