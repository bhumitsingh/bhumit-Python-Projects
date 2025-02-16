import sqlite3 as sql

connection = sql.connect("login_data.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
username TEXT NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL
)''')

connection.commit()

example_data = [
    ("Bhumit Singh", "bhumitsingh123", "chiragsingh360@gmail.com", "password123")
]

cursor.executemany(
    "INSERT INTO users (name, username, email, password) VALUES (?, ?, ?, ?)",example_data
)
connection.commit()
