#vd3.py
# Cho 2 dãy số
# In ra các phần tử thuộc dãy 1 mà ko thuộc dãy 2
lst1 = [1, 2, 3, 5, 7, 8, 10]
lst2 = [2, 4, 6, 8, 10]

for x in lst1:
    if x not in lst2:            
        print(x)
