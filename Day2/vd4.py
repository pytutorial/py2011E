#vd4
# Phân loại sản phẩm online theo điểm đánh giá TB
#  < 2.5 :          Kém
#  2.5 - <3.75:     TB
#  3.75 - <4.5:     Tốt
#  4.5+       :     Rất tốt

diemtb = float(input('Điểm đánh giá TB sản phẩm (0-5):'))
if diemtb < 2.5:
    print('Sản phẩm kém')
elif diemtb < 3.75:
    print('Sản phẩm TB')
elif diemtb < 4.5:
    print('Sản phẩm tốt')
else:
    print('Sản phẩm rất tốt')
