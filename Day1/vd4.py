#vd4.py
# Cho 2 điểm trên mặt phẳng có tọa độ (x1,y1) và (x2,y2)
# Yêu cầu : Tính khoảng cách giữa 2 điểm

# Input
x1 =  input('x1 = ')
y1 =  input('y1 = ')
x2 =  input('x2 = ')
y2 =  input('y2 = ')


# Process
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

dx = x1 - x2
dy = y1 - y2
distance = (dx** 2 + dy** 2) ** 0.5

# Output
print('Khoảng cách :', distance)
