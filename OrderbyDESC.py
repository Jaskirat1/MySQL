import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database  = 'mynewdb'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY address DESC"


mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)