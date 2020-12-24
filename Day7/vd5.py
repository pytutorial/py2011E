# vd5.py
# Trên 1 đường thẳng có các máy phát sóng tx_list, bán kính phát sóng R
# Các điểm thu sóng rx_list
# In ra các điểm ko nhận được tín hiệu

tx_list = [ 5, 10, 15, 20, 25, 30]   # transmitters
R = 1.5
rx_list = [1, 3, 7, 12, 17, 21, 27]  # receivers

def is_black_spot(x):  # True/False
    for t in tx_list:
        if abs(t-x) <= R:
            return False

    return True

for x in rx_list:
    if is_black_spot(x):
        print(x)
