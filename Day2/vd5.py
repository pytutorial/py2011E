# vd5.py
# Nhập vào GDP bình quân đầu người /năm của  1 nước
# TODO : In ra nước đó nằm trong nhóm nào
# https://blogs.worldbank.org/opendata/new-country-classifications-income-level-2019-2020

gdp = float(input('GDP bình quân đầu người/năm:'))

if gdp < 1026:
    print('Thu nhập thấp')
elif gdp < 3996 :
    print('Thu nhập TB thấp')
elif gdp < 12376 :
    print('Thu nhập TB cao')
else:
    print('Thu nhập cao')
    
