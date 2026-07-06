import sqlite3

DB_NAME = "virtual_friend.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():

    conn = get_connection()
    cursor = conn.cursor()

    # Chat history table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Mood history table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mood_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emotion TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def save_chat(role, message):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_history(role, message)
        VALUES (?, ?)
        """,
        (role, message)
    )

    conn.commit()
    conn.close()