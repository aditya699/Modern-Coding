'''
For this chatbot we will use a sqllite database for orders


'''

import sqlite3

def create_database():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # Create the orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT,  
            customer_name TEXT,
            order_date TEXT,
            order_status TEXT,
            order_total REAL
        )
    ''')
    
    # Insert sample data - 10 rows of order data
    sample_orders = [
        ('123456', 'John Doe', '2023-01-01', 'Delivered', 100.00),
        ('789012', 'Jane Smith', '2023-01-15', 'Pending', 75.50),
        ('345678', 'Robert Johnson', '2023-02-03', 'Shipped', 250.99),
        ('901234', 'Emily Davis', '2023-02-10', 'Processing', 45.25),
        ('567890', 'Michael Brown', '2023-02-22', 'Delivered', 180.75),
        ('234567', 'Sarah Wilson', '2023-03-05', 'Cancelled', 60.00),
        ('890123', 'David Taylor', '2023-03-18', 'Delivered', 125.49),
        ('456789', 'Jennifer Martinez', '2023-04-02', 'Shipped', 95.30),
        ('012345', 'Thomas Anderson', '2023-04-15', 'Pending', 210.25),
        ('678901', 'Lisa Garcia', '2023-04-30', 'Processing', 150.00)
    ]
    
    cursor.executemany('''
        INSERT INTO orders (order_id, customer_name, order_date, order_status, order_total)
        VALUES (?, ?, ?, ?, ?)
    ''', sample_orders)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

create_database()
    
    


