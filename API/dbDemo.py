import mysql.connector
from API.utilities.configurations import *

# host, dbname,user,password
'''conn = mysql.connector.connect(host='localhost', database='basavanagouda',user='root',
                               password='abc9741090584@J',)'''
conn=getConnection()
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from user1')
row=cursor.fetchone()
print(row)
'''cursor.execute('show databases')
for i in cursor:
    print(i)'''

'''cursor.execute('show tables')
for i in cursor:
    print(i)

cursor.execute('select * from orders')
row=cursor.fetchone()
print(row)
rows=cursor.fetchall()
print(rows[1])
sum=0
for row in rows:
    sum=sum+row[1]
print(sum)
'''
