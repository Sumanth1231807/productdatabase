import sqlite3
connection=sqlite3.connect("company.db")
getdesg=input("enter desg to be searched ")
result=connection.execute("select * from employee")


for i in result:
    print("name",i[1])
    print("designation",i[2])
    print("salary",i[3])
    print("companyname",i[4])
    print("mobilenumber",i[5])