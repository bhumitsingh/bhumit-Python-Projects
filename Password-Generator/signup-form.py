import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

conn = sql.connect("login_data.db")
cursor = conn.cursor()

def open_signup():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("300x200")
 
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
    entry_name.pack()

    # Password
    tk.Label(signup_window, text="Password").pack()
    entry_new_password = tk.Entry(signup_window)
    entry_new_password.pack()

    def register_user():
        name = entry_name.get()
        username = entry_new_username.get()
        email = entry_email.get()
        password = entry_new_password.get()

    if name and username and email and password:
        conn.connect_db()
        cursor = conn.cursor()

        # Check if username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists")
            conn.close()
            return
    
        # Insert new user into database
        cursor.execute("INSERT INTO users (name, username, email, password) VALUES (?, ?, ?, ?)" ,(name, username, email, password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Signup Successful")
        signup_window.destroy()
    else: 
        messagebox.showerror("Error","All fields are required")

# Signup Button
signup_button = tk.Button(signup_window, text="Register", command=register_user)
signup_button.pack()