import sqlite3
import os

def init_db(db_path="ibra_os/database/garage_memory.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clients table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        vehicle TEXT
    )
    ''')

    # Appointments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        date TEXT,
        status TEXT,
        FOREIGN KEY (client_id) REFERENCES clients (id)
    )
    ''')

    # Parts orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS part_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        part_name TEXT,
        quantity INTEGER,
        status TEXT
    )
    ''')

    conn.commit()
    conn.close()
    print(f"Database initialized at {db_path}")

if __name__ == "__main__":
    init_db()
