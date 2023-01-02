import mysql.connector


mydb = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password='',
    database ='mynewdb'
)



mycursor = mydb.cursor()

#mycursor.execute('CREATE DATABASE mynewdb')
"""mycursor.execute('SHOW DATABASES')

for x in mycursor:
    print(x)"""

#print(mydb)

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute('SHOW TABLES')
"""
for x in mycursor:
    print(x)"""

#PRIMARY KEY 
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

"""sql  = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Harleen Kaur', "Samrala road"),
    ("Gurvir Kaur", "Noorpur"),
    ("Kamaljeet Kaur", "Fatehgarg"),
    ("Parsanjeet Kaur", "Sirhind"),
    ("Tejinder Kaur", " Malhar road"),
    ("Kirandeep Kaur", "Model town"),
    ("Manmeet Kaur", "Ambala"),
    ("Jashandeep Kaur", "Delhi"),
    ("Amandeep Kaur", "Ferozpur road")
    
]
"""
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michele","Mohali")

mycursor.executemany(sql,val)

mydb.commit()"""

#print(mycursor.rowcount, "RECORD INSERTED!")

#print("Last inserted id is :-", mycursor.lastrowid)




