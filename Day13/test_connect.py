import MySQLdb

db_host = '127.0.0.1' # 34.122.175.106
db_user = 'admin'
db_password = 'abc@123'
db_name = 'py2011E'  # Dùng tên db name trên máy localhost
 
db = MySQLdb.connect(db_host, db_user, db_password, db_name)
print('Connected')