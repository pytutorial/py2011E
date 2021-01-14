# Chay chuong trinh he thong & lay ket qua tra ve
import subprocess

#result = subprocess.getoutput('ping google.com')       # windows
result = subprocess.getoutput('ping -c 4 google.com')  # mac/linux
lines = result.split('\n')
for line in lines:
    token = 'time='
    if token in line:
        pos = line.find(token) + len(token)
        line = line[pos:]
        time = line.split()[0]
        print(time)