import pymysql as sql

# To install the pymysql package, you can run the following in your terminal:
# pip install pymysql

# <----------------- Establishing the connection we need -------------->
# Server Name => localhost (it’s the default local server, used for development)
# username => 'root' (the default username for MySQL is usually 'root')
# password => '' (empty password, assuming you're using a local server with no password set for the 'root' user)

my_obj = sql.connect(host="localhost", user="root", password="")

# Creating a cursor object, which allows us to interact with the database
cursor_obj = my_obj.cursor()

# Try block to execute the SQL query and create the database
try:
    # SQL query to create a database named 'student'
    db = "CREATE DATABASE student"
    
    # Executing the SQL query
    cursor_obj.execute(db)
    
    # If successful, print a success message
    print('Database created successfully...')

except sql.MySQLError as e:
    # If there’s an error, catch it and print the error message
    print(f"Database connection error: {e}")

finally:
    # Close the cursor and connection objects to clean up resources
    cursor_obj.close()
    my_obj.close()
