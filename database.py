import sqlite3

DB_NAME = 'chatbot.db'

def init_db():
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    user_message TEXT,
                    bot_response TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def log_session(user_id, user_message, bot_response):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO sessions (user_id, user_message, bot_response) 
                VALUES (?, ?, ?)
            ''', (user_id, user_message, bot_response))
    except sqlite3.Error as e:
        print(f"Database error: {e}")