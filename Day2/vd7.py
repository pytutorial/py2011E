#vd7 : Nhập vào tuổi & giới tính 1 người
# YC: Kiểm tra người đó có trong tuổi LĐ ?
# (Nam : 18-60, Nữ : 18-55)

tuoi = int(input('Tuổi:'))
gioitinh = input('Giới tính (M/F):')

#if gioitinh  == 'M':
#    tuoi_nghi_huu = 60
#else:
#    tuoi_nghi_huu = 55
tuoi_nghi_huu = 60 if giotinh == 'M' else 55
    
if 18 <= tuoi <= tuoi_nghi_huu:
    print('Trong tuổi LĐ')
else:
    print('Ngoài tuổi LĐ')
