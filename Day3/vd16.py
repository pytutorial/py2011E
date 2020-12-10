# vd16
# Chạy chương trình nhiều lần (ko cần khởi động lại)

run = True
while run:
    a = float(input('Số thứ nhất:'))
    b = float(input('Số thứ hai:'))
    c = a + b
    print(f'{a}+{b}={c}')

    run = input('Tiếp tục (Y/N):') == 'Y'
