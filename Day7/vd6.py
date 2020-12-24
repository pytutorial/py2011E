# Nhập vào 1 số có 3 chữ số
# In ra phát âm tiếng Việt của số đó
# VD: 305 --> ba trăm lẻ năm
#     434 --> bốn trăm ba mươi tư

bang_so = ['không', 'một', 'hai', 'ba',
            'bốn', 'năm', 'sáu', 'bảy',
           'tám',  'chín', 'mười']

bang_so_2 = {0: '', 1: 'mốt', 5: 'lăm'}

def num_to_text_1d(x):
    return bang_so[x]

def num_to_text_2d(x):
    chuc =  x//10
    donvi = x%10
    if chuc == 1:  # 10-19
        if donvi in [0,5]:
            return f'mười {bang_so_2[donvi]}'
        else:
            return f'mười {bang_so[donvi]}'
    else: #20-99
        if donvi in [0,1,5]:
            return f'{bang_so[chuc]} mươi {bang_so_2[donvi]}'
        else:
            return f'{bang_so[chuc]} mươi {bang_so[donvi]}'

def num_to_text_3d(x):
    tram = x // 100
    chuc = (x//10)%10
    donvi = x%10

    if chuc == 0 and donvi == 0:  #100
        return f'{bang_so[tram]} trăm'

    if chuc == 0:                #101-109
        return f'{bang_so[tram]} trăm lẻ {bang_so[donvi]}'

    return f'{bang_so[tram]} trăm {num_to_text_2d(x%100)}'

def num_to_text(x):
    if 0 <= x < 10: return num_to_text_1d(x)
    if 10 <= x < 100: return num_to_text_2d(x)
    if 100 <= x < 1000: return num_to_text_3d(x)

for x in range(0, 1000):
    print(x, '-->', num_to_text(x))    



    
