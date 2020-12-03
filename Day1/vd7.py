# Máy ATM có 3 loại tiền 100K, 50K, 10K (số lượng ko giới hạn)
# Một người cần rút một số tiền M ( chia hết 10)
# Yêu cầu : In ra số tiền mỗi loại cần trả sao cho tổng số tờ là ít nhất

# Input
M = int(input('Số tiền cần rút:'))

# Process
n_100 = M // 100

M %= 100                # M = M % 100
n_50 = M // 50

M %= 50                 # M = M % 50
n_10 = M // 10

# Output
print(f'Sô tờ 100k: {n_100}, số tờ 50k : {n_50}, số tờ 10k: {n_10}')
