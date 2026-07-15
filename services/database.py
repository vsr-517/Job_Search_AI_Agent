import sqlite3

DB_PATH = "data/jobs.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS saved_jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            url TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_job(title, company, location, url):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO saved_jobs (title, company, location, url)
        VALUES (?, ?, ?, ?)
    """, (title, company, location, url))

    conn.commit()
    conn.close()


def get_saved_jobs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT title, company, location, url FROM saved_jobs")
    jobs = cursor.fetchall()

    conn.close()
    return jobs