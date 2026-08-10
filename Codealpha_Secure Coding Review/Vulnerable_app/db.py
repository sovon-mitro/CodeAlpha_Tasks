import sqlite3


DATABASE = "users.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_user(username, email, password):

    connection = get_connection()

    cursor = connection.cursor()

    query = f"""
        INSERT INTO users (username, email, password)
        VALUES ('{username}', '{email}', '{password}')
    """

    cursor.execute(query)

    connection.commit()
    connection.close()


def find_user(username):

    connection = get_connection()

    cursor = connection.cursor()

    query = f"""
        SELECT * FROM users
        WHERE username = '{username}'
    """

    cursor.execute(query)

    user = cursor.fetchone()

    connection.close()

    return user