# import pymysql
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spider DEFAULT CHARACTER SET utf8")
# db.close()

# import pymysql
#
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spider')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (ID))'
# cursor.execute(sql)
# db.close()

import pymysql

id = '201200011'
user = 'Bbbob1'
age = 21

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spider')
cursor = db.cursor()
sql = "INSERT INTO students(id, name, age) values(%s, %s, %s)"

try:
    cursor.execute(sql, (id, user, age))
    print('Successful')
    db.commit()
except:
    db.rollback()
db.close()

import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spider')
cursor = db.cursor()

data = {
    'id': '201dd20012',
    'name': 'BOb',
    'age': 25
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    db.rollback()
db.close()