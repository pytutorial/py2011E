# vd3.py
# Chuẩn hóa danh từ riêng
# Nhập vào danh từ riêng
# Yêu cầu : viết hoa các chữ cái đầu tiên của các từ đơn

danh_tu = input('Danh từ:')
items = danh_tu.split()

result = ''
for word in items:
    #print(word[0].upper(), word[1:])
    result += word[0].upper() + word[1:] + ' '

print(result)
