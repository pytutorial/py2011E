# vd7.py
# Cho đoạn văn bản (nhiều dòng)
# Cho một từ tìm kiếm (keywword)
# Yêu cầu: In ra vị trí dòng&cột mà keyword xuất hiện trong VB

st = '''Tối 14/12, Bộ Y tế thông tin nước ta có 5 ca mắc Covid-19 mới, đều là người nhập cảnh được cách ly ngay tại Ninh Bình, Thái Bình và Đồng Tháp.
Tính từ 18h ngày 13/12 đến 18h ngày 14/12, Việt Nam có 5 ca mắc Covid-19 mới, đều là ca nhập cảnh được cách ly ngay tại tỉnh Thái Bình (2), Đồng Tháp (2), Ninh Bình (1).'''

keyword = 'Covid-19'
#print(st)

lines = st.split('\n')

for i in range(len(lines)):
    line = lines[i]
    #print(f'Dòng {i+1}:', line)
    j = line.find(keyword)
    if j >= 0:
        print(f'Dòng :{i+1}, cột : {j+1}')


