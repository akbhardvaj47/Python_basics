# -------------Steps to create database connection in python------------
# step 1- Install Database Driver (pip install mysql-connector-python)
# step 2- Import the Required Library(import mysql.connector)
# step 3- Establish the Database Connection
# step 4- Handling Exceptions
# step 5- Closing the Connection

# Connect to MySQL database
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)

# Create a cursor object using the connection
cursor = connection.cursor()

# Perform operations (e.g., create table, insert data)
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))')
connection.commit()

# Close the connection
cursor.close()
connection.close()
