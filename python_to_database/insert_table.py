import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="mysql"
)


cursor=db.cursor()
sql="insert into student values(100,'amal','bcom',95)"
cursor.execute(sql)
db.commit()
db.close()
print("value inserted")