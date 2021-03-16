import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="mysql"
)


cursor=db.cursor()
f=open("emp_details","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into employee values(%s,%s,%s,%s)"
    cursor.execute(sql,data)
    db.commit()
