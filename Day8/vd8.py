#vd8
#Cho 1 file văn bản (tương đối lớn)
#Cho số N
#Yêu cầu : cắt file gốc thành nhiều file nhỏ sao cho:
#  - Mỗi file có không quá N kí tự
#  - Không cắt vào giữa dòng
input_file = 'input.txt'
N = 1000

#TODO: Doc tung dong cua file input.txt va in ra
acc = ''
fi = open(input_file, encoding='utf-8')
i = 0

def write_file(file_name, content):    
    fo = open(file_name, 'w', encoding='utf-8')
    fo.write(content)
    fo.close()
          
for line in fi:
    if len(acc) + len(line) > N:
        print(acc)        
        write_file(f'output_{i}.txt', acc)
        i += 1
        acc = ''        
    acc += line

if acc != '':
    write_file(f'output_{i}.txt', acc)
    
fi.close()
