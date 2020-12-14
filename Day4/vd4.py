# vd4.py
# Nhập vào một xâu dạng dd/mm/yyyy
# In ra : ngày, tháng, năm
st = input('Ngày tháng (dd/mm/yyyy):')
items = st.split('/')
print('Ngày:', items[0])
print('Tháng:', items[1])
print('Năm:', items[2])
