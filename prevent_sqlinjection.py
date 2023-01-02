import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database  = 'mynewdb'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
val = ("Mohali", )

mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)