#vd8.py
# Cho danh sách điểm trên mặt phẳng
# Tính độ dài đường gấp khúc kín tạo bởi các điểm
lst = [
    (1, 2),
    (3, 4),
    (4, 5),
    (5, 1),
    (6, 2),
    (7, 5)
]

distance = 0
for i in range(len(lst)):
    x1, y1 = lst[i]
    x2, y2 = lst[(i+1)%len(lst)]
    distance += ((x1-x2)**2 + (y1-y2)**2)**0.5

print(round(distance,2))    
