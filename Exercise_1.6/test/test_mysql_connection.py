import mysql.connector

# Connect to MySQL server and database
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',          
    passwd='password',        
    database='my_database'     
)

cursor = conn.cursor()

try:
    # 1. Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock (
            item_id INT PRIMARY KEY AUTO_INCREMENT,
            item_name VARCHAR(50),
            manufacturer_name TEXT,
            price FLOAT,
            quantity INT
        )
    ''')
    print("Table 'stock' ready.")

    # 2. Insert some data (use placeholders to avoid SQL injection)
    sql_insert = '''
        INSERT INTO stock (item_name, manufacturer_name, price, quantity) 
        VALUES (%s, %s, %s, %s)
    '''
    values = [
        ('Water', 'Aquafina', 10.0, 20),
        ('Coca-Cola', 'The Coca-Cola Company', 2.5, 30),
        ('Bread', 'Kingsmill', 15.0, 30)
    ]
    cursor.executemany(sql_insert, values)
    print(f"Inserted {cursor.rowcount} rows.")

    # Commit the inserts
    conn.commit()

    # 3. Query and display all rows
    cursor.execute("SELECT * FROM stock")
    results = cursor.fetchall()
    print("\nCurrent Stock Table:")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Manufacturer: {row[2]}, Price: {row[3]}, Quantity: {row[4]}")

    # 4. Update price of Bread to 35 where item_id = 3
    cursor.execute("UPDATE stock SET price = 35 WHERE item_id = 3")
    print("\nUpdated Bread price to 35.")
    conn.commit()

    # 5. Delete the item with item_id = 2 (Coca-Cola)
    cursor.execute("DELETE FROM stock WHERE item_id = 2")
    print("Deleted item with ID 2.")
    conn.commit()

    # 6. Query again to show changes
    cursor.execute("SELECT * FROM stock")
    results = cursor.fetchall()
    print("\nStock Table after updates:")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Manufacturer: {row[2]}, Price: {row[3]}, Quantity: {row[4]}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection safely
    cursor.close()
    conn.close()
    print("\nConnection closed.")
