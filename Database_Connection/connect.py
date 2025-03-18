import mysql.connector

# Establish a connection to the MySQL/MariaDB database
print('Connection starting....')
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student"
    )
    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query (e.g., create a table)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))''')

    # Insert data
    cursor.execute('''INSERT INTO users (name) VALUES (%s)''', ("Amit Bhardwaj",))

    # Commit the changes and close the connection
    conn.commit()

    # Query the data
    cursor.execute('''SELECT * FROM users''')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print('Connection successfully')
except Exception as e:
    print(e)
finally:
    # Close the connection
    cursor.close()
    conn.close()
