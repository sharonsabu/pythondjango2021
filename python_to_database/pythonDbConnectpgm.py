#install mysql-connector
#step1 import package
import mysql.connector


#step2 establish connection

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123"
)

#create cursor object
cursor=db.cursor()
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)

