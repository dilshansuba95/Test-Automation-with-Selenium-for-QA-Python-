import sqlite3

# Function to retrieve test results
def get_test_results():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM test_results')
    results = cur.fetchall()
    conn.close()
    return results

# Display test results
results = get_test_results()
for result in results:
    print(result)