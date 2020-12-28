# vd7.py
# Tao chuong trinh soan thao
# Nhap vao tung dong --> luu vao file
# Gap chuoi "exit()" --> dong file

filename = 'output.txt'
f = open(filename, 'w', encoding='utf-8')

while True:
    line = input('')
    if line.strip() != 'exit()':
        #TODO: Ghi vao file
        f.write(line + '\n')
    else:
        break

f.close()
