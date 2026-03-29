import sqlite3
import os

# Find the database path
app_data = os.environ.get('LOCALAPPDATA', os.path.expanduser('~'))
base_dir = os.path.join(app_data, 'CRAB_AI')
# Fallback to local if not found (for script mode)
db_paths = [
    os.path.join(base_dir, 'database.db'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
]

for db_path in db_paths:
    if os.path.exists(db_path):
        print(f"Checking database at: {db_path}")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check if doc_name exists
            cursor.execute("PRAGMA table_info(history)")
            columns = [info[1] for info in cursor.fetchall()]
            
            if 'doc_name' not in columns:
                print("Adding 'doc_name' column to 'history' table...")
                cursor.execute("ALTER TABLE history ADD COLUMN doc_name TEXT")
                conn.commit()
                print("Migration successful!")
            else:
                print("'doc_name' column already exists.")
                
            conn.close()
        except Exception as e:
            print(f"Error migrating database: {e}")
    else:
        print(f"Database not found at: {db_path}")

print("Done.")
