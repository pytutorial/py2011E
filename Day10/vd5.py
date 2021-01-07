#Đọc file csv
import csv
with open('bangdiem.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    data_rows = list(reader)

print(header_row)
result_rows = []
for row in data_rows: 
    ho_ten, diem_hs1, diem_hs2, diem_hs3 = row
    diem_tb = (int(diem_hs1) + 2*int(diem_hs2) + 3*int(diem_hs3))/6
    print(ho_ten, round(diem_tb,1))
    result_rows.append([ho_ten, round(diem_tb,1)])

with open('ketqua.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Họ và tên', 'Điểm TB'])
    writer.writerows(result_rows)

