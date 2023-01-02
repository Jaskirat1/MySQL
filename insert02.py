import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database  = 'mynewdb'
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name) VALUE (%s)"
val = ['Amit']

mycursor.execute(sql, val)
mydb.commit()


