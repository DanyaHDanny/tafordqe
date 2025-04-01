import psycopg2
from psycopg2 import sql

# Database connection details
DB_HOST = "postgres"
DB_PORT = 5432
DB_NAME = "jenkins_db"
DB_USER = "jenkins"
DB_PASSWORD = "jenkins_password"

# Data to insert
data = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com"),
]

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Insert data into the table
    insert_query = sql.SQL("""
        INSERT INTO users (name, email) VALUES (%s, %s);
    """)
    for row in data:
        cursor.execute(insert_query, row)

    # Commit the transaction
    conn.commit()

    print("Data generated successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()