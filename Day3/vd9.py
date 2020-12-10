# vd9.py
# Cho danh sách điểm thu sóng trên 1 đường thẳng
# Cho danh sách các điểm phát sóng
# Bán kính phủ sóng của mỗi điểm phát là R
# In ra các điểm thu ko nhận được tín hiệu
dsThu = [1, 5, 7, 10, 15, 20]
dsPhat = [ 3, 6, 8, 12, 18]
R = 2
for dt in dsThu:
    koTinHieu = True

    for dp in dsPhat:
        if abs(dt-dp) <= R: # có tín hiệu
            koTinHieu = False
            break    

    if koTinHieu:
        print(dt)    
            
