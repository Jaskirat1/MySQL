import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = 'mynewdb'

)

mycursor  = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)