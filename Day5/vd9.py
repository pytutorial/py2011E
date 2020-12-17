# vd9.py
# Cho 1 điểm (x,y)
# Cho 1 danh sách điểm [(xi,yi)]
# Tìm điểm trong danh sách gần nhất (x,y)

x, y = 10, 10
points = [
    (4,5),
    (5, 6),
    (7, 6),
    (8, 5),
    (14, 15),
    (15,13),
    (12, 16),
]
d_min = float('inf')
for point in points:
    xi, yi = point
    d = ((xi-x)**2 + (yi-y)**2)**0.5
    if d < d_min:
        d_min = d
        x_min = xi
        y_min = yi
print(x_min, y_min, d_min)
        
