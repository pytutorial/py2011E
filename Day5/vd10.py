#vd10.py
# CHo 2 dãy số
# In ra các số thuộc dãy 1 nhưng ko thuộc dãy 2

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [2, 4, 6, 8, 10]

print([x for x in lst1 if x not in lst2])
