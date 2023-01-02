import mysql.connector 


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'mynewdb'
)


mycursor = mydb.cursor()

sql = "UPDATE customers SET name ='Gurveer Kaur' WHERE address = 'Noorpur'"

mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "Record affected")