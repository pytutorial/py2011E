# vd2.py
# Cho 1 dãy số
# Tách dãy số thành 2 dãy mới : chẵn & lẻ

lst = [1, 2, 4, 5, 8, 9, 10, 12, 13, 15]
lst_chan = []
lst_le = []

#HINT: append
for x in lst:
    if x%2 ==0:
        lst_chan.append(x)   # lst_chan <- x
    else:
        lst_le.append(x)     # lst_le <- x

print('lst_chan=', lst_chan)
print('lst_le=', lst_le)
