# vd6.py
# Nhập vào chiều cao (mét) & cân nặng(kg) của 1 người
# Tính bmi = can_nang/(chieu_cao ** 2)
# Phân loại bmi :
#   < 16:         Gầy
#   16 - <18.5  : Hơi gầy
#   18.5 - < 25 : Bình thường
#   25   - < 30 : Hơi béo
#   30 +        : Béo (phì)

h = float(input('Chiều cao (mét):'))
m = float(input('Cân nặng (kg):'))
bmi = m/h/h
print('bmi=', bmi)
#TODO : Đánh giá bmi
if bmi < 16:
    print('Thân hình gầy')
elif bmi < 18.5:
    print('Thân hình hơi gầy')
elif bmi < 25:
    print('Thân hình bình thường')
elif bmi < 30:
    print('Thân hình hơi béo')
else:
    print('Thân hình béo')
