# import mysql.connector

# # Replace with your database credentials
# host = "127.0.0.1"
# user = "root"
# password = "root123"
# database = "sys"

# # Establish a connection
# conn = mysql.connector.connect(
#     host=host,
#     user=user,
#     password=password,
#     database=database
# )

# # Create a cursor
# cursor = conn.cursor()

# # Example SQL query to create the 'Customers' table
# create_table_query = """
# CREATE TABLE Customers (
#     CustomerID INT PRIMARY KEY,
#     FirstName VARCHAR(255),
#     LastName VARCHAR(255),
#     Email VARCHAR(255),
#     PhoneNumber VARCHAR(20)
# )
# """

# # Execute the create table query
# cursor.execute(create_table_query)

# # Commit the changes to the database
# conn.commit()

# # Example SQL query for inserting data into the 'Customers' table
# insert_data_query = """
# INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber)
# VALUES (%s, %s, %s, %s, %s)
# """

# # Data to be inserted
# data_to_insert = (4, "Jiji", "Gomez", 'jiji@gmail.com', '46765587')

# # Execute the insert query
# cursor.execute(insert_data_query, data_to_insert)

# # Commit the changes to the database
# conn.commit()

# # Close the cursor and connection
# cursor.close()
# conn.close()


import mysql.connector

host = "127.0.0.1"
user = "root"
password = "root123"
database = "sys"

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()

# Example SQL query for inserting data into the 'Demo' table
sql = "INSERT INTO Demo(DemoID, FirstName, Address, PostalCode, Country, City) VALUES (%s, %s, %s, %s, %s, %s)"
val = (6, "Suja", "Attupurath", 12345, "India", "Adoors")
# print("SQL Query:", sql)
# print("Values:", val)
cursor.execute(sql, val)


# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
