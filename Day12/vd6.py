# Handle exception
import traceback
while True:
    try:
        x = input('Số thứ nhất:')
        y = input('Số thứ hai:')
        
        x = int(x)
        y = int(y)
        print('Tổng 2 số:', x+y)

        c = input('Tiếp tục (Y/N):')
        if c.upper() != 'Y':
            break

    except: # Exception as e:
        traceback.print_exc() #print('Lỗi :', e)
    