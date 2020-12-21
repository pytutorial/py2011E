# vd4.py
# Nhập vào phát âm tiếng Việt của 1 số từ 1-10
# In ra số đó
# VD: năm -> 5

phat_am_so = input('Phát âm của số:')
table = {
    'một': 1,
    'hai': 2,
    'ba':  3,
    'bốn': 4,
    'năm': 5,
    'sáu': 6,
    'bảy': 7,
    'tám': 8,
    'chín': 9,
    'mười': 10
}
print(table.get(phat_am_so.lower(), 'không tồn tại'))
