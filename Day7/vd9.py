st = '''Hom nay o Ha Noi phat hien 10 ca Covid, cac ca Covid deu la khach du lich
        O TP.HCM cung phat hien 20 ca Covid'''

keyword = 'Covid'

def search_line(line, keyword):  # return all positions
    if keyword not in line:
        return []

    pos = line.find(keyword)     # first position
    other_pos_list = search_line(line[pos+len(keyword):], keyword)
    return [pos] + [pos+len(keyword)+ x for x in other_pos_list]

lines = st.split('\n')
for row in range(len(lines)):
    col_list = search_line(lines[row], keyword)
    for col in col_list:
        print(row, col)

