import sqlite3
import time  # Optional for pausing between Selenium actions

# Connect to the database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Execute a query to retrieve data (replace with your desired query)
cursor.execute("SELECT * FROM test_results")

# Fetch results
rows = cursor.fetchall()

# Print the results (modify for your table structure)
for row in rows:
    print(f"id: {row[0]} | test_name: {row[1]} | status: {row[2]} | timestamp: {row[3]}\")
    #id INTEGER PRIMARY KEY AUTOINCREMENT,
    #test_name TEXT,
    #status TEXT,
    #timestamp TEXT

# Optional: Pause before proceeding with Selenium (if applicable)
time.sleep(5)

# Close the connection (important!)
conn.close()