import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="railway")

if(mydb):
    print("successful")
else:
    print("unsuccessful")

mycursor=mysql.cursor()
# mycursor.execute("create database college;")
mycursor.execute("show databases;")

for i in mycursor:
    print(i)

#mycursor.execute("create table student(ssn int,name varchar(10));")
mycursor.execute("insert into student values((1,'A'),(2,'B'),(3,'C'));")
mydb.commit()
mycursor.execute("select * from student;")
sql=mycursor.fetchall()
for i in sql:
    print(i)

res="update student set ssn=4 where name='B';"
mycursor.execute(res)
print("**after update**")
mycursor.execute('select * from student;')
sql=mycursor.fetchall()
for i in sql:
    print(i)

mycursor.close()
mydb.close()
print("MySQL connection is closed;")
