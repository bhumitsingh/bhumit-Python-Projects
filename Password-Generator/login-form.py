import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

# Database Initialization
conn = sql.connect("login_data.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
username TEXT NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL
)''')

conn.commit()

# Function to Connect to Database
def connect_db():
    return sql.connect("login_data.db")

# Login Function
def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    
    conn.close()

    if user:
        messagebox.showinfo("Login Success", f"Welcome, {user[0]}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Open Signup Window
def open_signup():
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_window.geometry("300x250")

    # Name
    tk.Label(signup_window, text="Name").pack()
    entry_name = tk.Entry(signup_window)
    entry_name.pack()

    # Username
    tk.Label(signup_window, text="Username").pack()
    entry_new_username = tk.Entry(signup_window)
    entry_new_username.pack()

    # Email
    tk.Label(signup_window, text="Email").pack()
    entry_email = tk.Entry(signup_window)
    entry_email.pack()

    # Password
    tk.Label(signup_window, text="Password").pack()
    entry_new_password = tk.Entry(signup_window, show="*")
    entry_new_password.pack()

    # Function to Store New User
    def register_user():
        name = entry_name.get()
        new_username = entry_new_username.get()
        email = entry_email.get()
        new_password = entry_new_password.get()

        if name and new_username and email and new_password:
            conn = connect_db()
            cursor = conn.cursor()

            # Check if username already exists
            cursor.execute("SELECT * FROM users WHERE username=?", (new_username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username already exists")
                conn.close()
                return

            # Insert New User
            cursor.execute("INSERT INTO users (name, username, email, password) VALUES (?, ?, ?, ?)", 
                           (name, new_username, email, new_password))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Signup Successful!")
            signup_window.destroy()  # Close Signup Window
        else:
            messagebox.showerror("Error", "All fields are required")

    # Signup Button
    btn_register = tk.Button(signup_window, text="Register", command=register_user)
    btn_register.pack()

# GUI Setup
root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

# Username
tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Password (Hidden Input)
tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Login Button
btn_login = tk.Button(root, text='Login', command=login)
btn_login.pack()

# Signup Button (Opens Signup Window)
btn_signup = tk.Button(root, text="Signup", command=open_signup)
btn_signup.pack()

root.mainloop()
