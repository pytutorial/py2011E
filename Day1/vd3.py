# vd3.py
# Nhập vào điểm hệ số 1, hệ số 2 , hệ số 3 của một học sinh
# Yêu cầu : In ra điểm trung bình của học sinh đó

# Input
diem_hs1 = input('Điểm hệ số 1:')
diem_hs2 = input('Điểm hệ số 2:')
diem_hs3 = input('Điểm hệ số 3:')

# Procees
diem_hs1 = float(diem_hs1)
diem_hs2 = int(diem_hs2)
diem_hs3 = int(diem_hs3)
diem_tb = (diem_hs1 + 2*diem_hs2 + 3*diem_hs3)/6

# Output
print('Điểm trung bình: ' , round(diem_tb, 1))
