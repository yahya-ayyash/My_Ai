import sqlite3
import os
import shutil
from datetime import datetime

DB_PATH = 'database.db'
BACKUP_DIR = 'backups'

def migrate():
    # 1. Create backup
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(BACKUP_DIR, f'database_backup_{timestamp}.db')
    
    if os.path.exists(DB_PATH):
        print(f"Creating backup at {backup_path}...")
        shutil.copy2(DB_PATH, backup_path)
    else:
        print("Database not found. Nothing to migrate.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # 2. Ensure chats table exists
        print("Ensuring 'chats' table exists...")
        cursor.execute('''CREATE TABLE IF NOT EXISTS chats 
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          user_id INTEGER,
                          title TEXT,
                          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                          FOREIGN KEY (user_id) REFERENCES users (id))''')

        # 3. Check for chat_id column in history
        cursor.execute("PRAGMA table_info(history)")
        columns = [row[1] for row in cursor.fetchall()]
        
        if 'chat_id' not in columns:
            print("Adding 'chat_id' column to 'history' table...")
            cursor.execute("ALTER TABLE history ADD COLUMN chat_id INTEGER REFERENCES chats(id)")
            print("Migration successful!")
        else:
            print("'chat_id' column already exists.")

        conn.commit()
    except Exception as e:
        print(f"Error during migration: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    migrate()