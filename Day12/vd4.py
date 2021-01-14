# Tham so dong lenh
import sys
print(sys.argv)

if len(sys.argv) < 3:
    print('Usage: copy.py <src file> <destination>')
    exit()

src = sys.argv[1]
dst = sys.argv[2]
print(f'Copying file from {src} to {dst} ....')