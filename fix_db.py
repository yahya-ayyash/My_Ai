import sqlite3
import os

DB_PATH = r"c:\Users\Admin\OneDrive\Documents\VISUAL STIDIO\website\database.db"

def fix():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS uploads_context 
                 (user_id INTEGER PRIMARY KEY, 
                  filename TEXT, 
                  content TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                  FOREIGN KEY (user_id) REFERENCES users (id))''')
    conn.commit()
    conn.close()
    print("Database table ensures/created successfully.")

if __name__ == "__main__":
    fix()
