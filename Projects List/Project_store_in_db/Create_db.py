import sqlite3
from datetime import datetime
import pytz

# Function to get the current time in Sri Lankan time zone
def get_sri_lankan_time():
    SL_timezone = pytz.timezone('Asia/Colombo')
    return datetime.now(SL_timezone).strftime('%Y-%m-%d %H:%M:%S:%p')

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('test.db')

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute('''
    CREATE TABLE IF NOT EXISTS test_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_name TEXT,
        status TEXT,
        timestamp TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()