import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="mysql"
)


cursor=db.cursor()
sql="create table employee(eid int, name varchar(50),salary int,des varchar(50))"
cursor.execute(sql)
print("table created")