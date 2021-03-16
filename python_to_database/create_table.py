import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="mysql"
)


cursor=db.cursor()
sql="create table student(roll int, name varchar(50),course varchar(50),total int)"
cursor.execute(sql)
print("table created")