# vd5.py
# Dân sô VN 2020 : 97.3
# Tốc độ tăng : 1.1%
# In ra dân số ước đoán từ năm 2021 - 2030

danso = 97.3
for nam in range(2021, 2031):
    luong_tang = danso * 1.1/100
    danso += luong_tang
    print(f'Dân số năm {nam} là {round(danso,1)} triệu người')
    
