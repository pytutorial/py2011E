# vd7: Lambda
# Sắp xếp dãy số theo giá trị tuyệt đối

def f(x):
    return abs(x)

lst = [1, 2, -3, 5, 4, -7, 6]
#lst = sorted(lst, key=f)
lst = sorted(lst, key=lambda x: abs(x)) 
print(lst)
