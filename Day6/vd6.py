#vd6
# CHo 1 văn bản
# In ra các từ đơn kèm theo số lần xuất hiện của mỗi từ

st = 'hôm nay là thứ hai , ngày mai là thứ ba'
counts = {}
for word in st.split():
    counts[word] = counts.get(word, 0) + 1

#for word in counts:
#    print(word, ':', counts[word])

count_items = counts.items()
#print(count_items)
count_items = sorted(count_items, reverse=True, key=lambda x:x[1])
print('=======')
for word, count in count_items:
    print(word, ':', count)
