import sqlite3 as sql

connection=sql.connect("Product.db")
#connection.execute('''create table product data(
#                        Product_Code integer,
#                        Product_name text,
#                        Product_price integer,
#                        Distributor_name text,
#                        manufacturer_name text
#                       );''')
#print("Table is created successfully")

getProductCode=input("Enter the Product code :")
getProductName=input("Enter the Product name :")
getProductPrice=input("Enter the Price of the product :")
getDistrName=input("Enter Distributor name :")
getManfactName=input("Enter Manufacturer name :")

connection.execute("insert into Product_data(Product_Code,Product_name,Product_price,Distributor_name,manufacturer_name) \
                    values("+getProductCode+",'"+getProductName+"',"+getProductPrice+",'"+getDistrName+"','"+getManfactName+"')")

connection.commit()
connection.close()


print("data is inserted successfully")

