# vd15
# Mô phỏng chuyện động của vật thể
# Ném vật từ mặt đất với vận tốc v
# Tìm độ cao cực đại

h = 0
v = 5.0
dt = 0.001
g = 9.8

while v > 0:
    v -= g*dt
    h += v*dt

print(h)    
