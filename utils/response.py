import asyncio
import sqlite3
import os
from dotenv import load_dotenv
from agents import Agent, Runner, trace, set_tracing_export_api_key

from agents import Agent, Runner, function_tool

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Set the tracing export API key
set_tracing_export_api_key(os.getenv("OPENAI_API_KEY")) # type: ignore

@function_tool
def get_order_status(order_id: str) -> str:
    try:
        # Check if database exists, create it if it doesn't
        if not os.path.exists('orders.db'):
            create_database()
            
        # Connect to the database
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()

        # Verify table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        if not cursor.fetchone():
            create_database()
            
        # Query the order status
        cursor.execute("SELECT order_status FROM orders WHERE order_id = ?", (order_id,))
        result = cursor.fetchone()

        # Close the connection
        conn.close()

        if result:
            return f"The order status for {order_id} is {result[0]}."
        else:
            return f"No order found with ID {order_id}."
    except sqlite3.Error as e:
        return f"Database error occurred: {str(e)}"
    except Exception as e:
        return f"An error occurred while checking order status: {str(e)}"
    
@function_tool

def request_callback(email_id: str) -> str:

    return "A call request has been assigned to customer support agent, they will reach you on 24 hrs"

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
    
    # Insert sample data
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

agent = Agent(
    name="Customer Support Agent",
    instructions="As a customer support agent, you can check the status of an order using the order ID. If a customer requests a callback, prompt them for their email address and utilize the request_callback tool to schedule a call with a customer support agent.",
    tools=[get_order_status, request_callback],
)

async def get_response(message: str, chat_history: list[dict]) -> str:
    print(chat_history)
    message="current message is "+message + " and the chat history is "+str(chat_history)
    result = await Runner.run(agent, input=message) #type: ignore
    return result.final_output

async def main():
    result = await get_response("Need to check order status for order 123456?", [])
    print(result)

if __name__ == "__main__":
    asyncio.run(main())