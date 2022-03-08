import sqlite3 as s
connection = s.connect("Company.db")
connection.execute(''' CREATE TABLE EMPLOYEE(
                        EMP_CODE INTEGER PRIMARY KEY AUTOINCREMENT,
                        EMP_NAME TEXT,
                        DESIGNATION TEXT,
                        SALARY INTEGER,
                        COMPANY_NAME TEXT,
                        MOBILE_NUMBER INTEGER


 ) ''')

print("Table created Successfully")

getEmpname = input("Enter Employee name: ")
getDesignation = input("Enter Designation: ")
getSalary = input("Enter Salary: ")
getCompanyname = input("Enter Company Name: ")
getMobileno = input("Enter Mobile Number: ")


connection.execute(" INSERT INTO EMPLOYEE(EMP_NAME, DESIGNATION, SALARY, COMPANY_NAME, MOBILE_NUMBER) \
 VALUES('"+getEmpname+"','"+getDesignation+"',"+getSalary+",'"+getCompanyname+"',"+getMobileno+")")
connection.commit()
connection.close()
print("Inserted Successfully")