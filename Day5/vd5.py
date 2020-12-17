#vd5.py
# Cho vị trị hiện tại x của 1 người trên 1 đường thẳng
# Cho danh sách các trạm (xăm/ATM) trên đường thẳng đó
# In ra vị trí của trạm gần nhất

x = 5
lst = [1, 3, 8, 10]

s_min = lst[0]          # tram gan nhat 
d_min = abs(x-s_min)    # khoang cach ngan nhat

for s in lst:
    d = abs(s-x)
    if d < d_min:
        d_min = d
        s_min = s

print(s_min, d_min)        
