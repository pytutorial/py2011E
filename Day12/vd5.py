# Viết  tool tìm kiếm file trong một thư mục : 
# Tham số 1 : Tên thư mục
# Tham số 2: Từ khóa tìm kiếm
import sys, os
if len(sys.argv) < 3:
    print('Usage: findfile.py <dir> <keyword>')
    exit()

indir = sys.argv[1]
keyword = sys.argv[2]

def searchFiles(d, term):
    items = os.listdir(d)
    for item in items:
        item_path = os.path.join(d, item)
        if os.path.isfile(item_path) and term.lower() in item.lower():
            print(item_path)
        
        if os.path.isdir(item_path):
            searchFiles(item_path, term)

# python vd5.py .. vd1
searchFiles(indir , keyword)