import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database  = 'mynewdb'
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE name = 'Rohit'"


mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "Records deleted")