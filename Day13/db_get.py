import MySQLdb
db_host = '127.0.0.1' # 34.122.175.106
db_user = 'admin'
db_password = 'abc@123'
db_name = 'py2011E'  # Dùng tên db name trên máy localhost
 
db = MySQLdb.connect(db_host, db_user, db_password, db_name, charset='utf8')
keyword = input('Nhập từ tìm kiếm (tên/mã học sinh):')
sql = """SELECT * FROM student 
        WHERE name LIKE %s 
        OR student_no LIKE %s """

cursor = db.cursor()  # keyword = ' OR 1=1 OR 1='
cursor.execute(sql, [f'%{keyword}%', f'%{keyword}%'])
result = cursor.fetchall()
for row in result:
    print(row)