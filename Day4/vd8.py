#vd8.py
# Cho 1 đoạn văn bản nhiều dòng
# Cho số N
# Yêu cầu: Format lại văn bản sao cho mỗi dòng ko quá N kí tự

st = '''Tối 14/12, Bộ Y tế thông tin nước ta có 5 ca mắc Covid-19 mới, đều là người nhập cảnh được cách ly ngay tại Ninh Bình, Thái Bình và Đồng Tháp.
Tính từ 18h ngày 13/12 đến 18h ngày 14/12, Việt Nam có 5 ca mắc Covid-19 mới, đều là ca nhập cảnh được cách ly ngay tại tỉnh Thái Bình (2), Đồng Tháp (2), Ninh Bình (1).'''

N = 80
lines = st.split('\n')

for line in lines:
    while len(line) > N:
        pos = N
        while pos > 0 and line[pos] != ' ': pos -= 1
        print(line[:pos])
        line = line[pos:]

    print(line)
