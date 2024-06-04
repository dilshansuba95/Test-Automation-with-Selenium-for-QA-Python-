import sqlite3
from selenium import webdriver
import time
from datetime import datetime
import pytz

# Function to get the current time in Sri Lankan time zone
def get_sri_lankan_time():
    SL_timezone = pytz.timezone('Asia/Colombo')
    return datetime.now(SL_timezone).strftime('%Y-%m-%d %H:%M:%S:%p')

# Function to store test results in the database
def store_test_result(test_name, status):
    try:
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO test_results (test_name, status, timestamp)
            VALUES (?, ?, ?)
        ''', (test_name, status, get_sri_lankan_time()))
        conn.commit()
        conn.close()
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")

# Set up Selenium WebDriver
driver = webdriver.Chrome()

try:
    # Example test: Open a website and check the title
    driver.get('https://google.com')
    time.sleep(2)
    
    if "Google" in driver.title:
        store_test_result('Test Example Domain Title', 'Pass')
    else:
        store_test_result('Test Example Domain Title', 'Fail')

    # Additional tests can be added here

except Exception as e:
    store_test_result('Test Example Domain Title', f'Fail: {e}')

finally:
    driver.quit()
