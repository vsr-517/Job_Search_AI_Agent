import sqlite3

DB_PATH = "data/jobs.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS saved_jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE
        )
        """
    )

    connection.commit()
    connection.close()


def save_job(title, company, location, url):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO saved_jobs (title, company, location, url)
            VALUES (?, ?, ?, ?)
            """,
            (title, company, location, url),
        )

        connection.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        connection.close()


def get_saved_jobs():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, company, location, url
        FROM saved_jobs
        ORDER BY id DESC
        """
    )

    jobs = cursor.fetchall()
    connection.close()

    return jobs


def delete_job(job_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM saved_jobs WHERE id = ?",
        (job_id,),
    )

    connection.commit()
    connection.close()