import mysql.connector

mydb = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = '',
    database = 'mynewdb'
)

mcursor = mydb.cursor()

mcursor.execute('SELECT name, address FROM customers')

myresult = mcursor.fetchall()

for x in myresult:
    print(x)