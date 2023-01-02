import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database  = 'mynewdb'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)