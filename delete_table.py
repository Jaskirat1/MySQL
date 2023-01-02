"""import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database  = 'mynewdb'
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

# we can also use IF EXISTS keyword to avoid getting error.

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

"""