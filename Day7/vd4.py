#vd4.py
#Viết hàm tính tổng các chữ số của 1 số tự nhiên
#Input : x - số tự nhiên
#Output : Tổng các chữ số

def sum_digit(x):
    s = 0
    while x > 0:
        digit = x%10
        s += digit
        x = x//10
    return s

def sum_digit_recursive(x):
    if x < 10:
        return x

    return sum_digit_recursive(x // 10) + x%10

print(sum_digit(43278498))
print(sum_digit_recursive(43278498))
