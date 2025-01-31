import json
import tkinter as tk
from tkinter import messagebox,ttk

# File to store tasks
TODO_FILE = 'todo_list.json'

# Categories and Priority Levels
CATEGORIES = ['Work', 'Personal', 'Study', 'Health', 'Shopping']
PRIORITIES = {"Low": "🟢", "Medium": "⚡", "High": "🔥"}

def load_tasks():
    try:
        with open(TODO_FILE, 'r') as file :
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get().strip()
    priority = priority_var.get()
    category = category_var.get()
    if task:
        tasks.append({"task": task, "done": False, "priority" : priority, "category" : category})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning('Warning', 'Task cannot be empty')

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]['done'] = True
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning('Warning', 'Select a task to mark as done')

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning('Warning', 'Select a task to remove')

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        priority_icon = PRIORITIES[task["priority"]]
        task_listbox.insert(tk.END, f"{status} {priority_icon} {task['task']} {task['category']}")

def unmark_selected():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]['done'] = False
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning('Warning', 'Select a task to unmark')

# Intialize GUI
root = tk.Tk() # Create a window
root.title('To-Do List') # Set the title

# Task entry
task_entry = tk.Entry(root, width=40) # Create an entry widget
task_entry.grid(row=0, column=0, padx=10, pady=10) # Place it in the window

#Priority Dropdown
priority_var = tk.StringVar(value = "Medium") # Default value
priority_dropdown = ttk.Combobox(root, textvariable=priority_var, values=list(PRIORITIES.keys()), width=10, state = 'readonly') # creates a dropdown widge of width 10 in readonly mode with priority levels
priority_dropdown.grid(row=0, column=1, padx=5, pady=10) # Place it next to the task entry

# Category Dropdown
category_var = tk.StringVar(value = "Work") # Default value
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=CATEGORIES, width=10, state = 'readonly') # creates a dropdown widget of width 10 in readonly mode with categories
category_dropdown.grid(row=0, column=2, padx=5, pady=10) # Place it next to the priority dropdown

# Add task button
add_button = tk.Button(root, text='Add Task', command=add_task)
add_button.grid(row=0, column=3, padx=5, pady=10)

# Unmark button
unmark_button = tk.Button(root, text='Unmark', command=unmark_selected)
unmark_button.grid(row=2, column=1, padx=10, pady=10)

# Task listbox
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Category Filter Dropdown
filter_var = tk.StringVar(value = "All") # Default value
filter_dropdown = ttk.Combobox(root, textvariable=filter_var, values=["All"]+CATEGORIES, width=10, state = 'readonly') # Add "All" option
filter_dropdown.grid(row=2, column=0, padx=5, pady=10) # Place it below the task listbox
filter_dropdown.bind("<<ComboboxSelected>>", lambda e: update_task_list()) # Update task list when filter changes


# Done and Remove buttons
done_button = tk.Button(root, text='Mark as Done', command=mark_done)
done_button.grid(row=2, column=0, padx=5, pady=10)

remove_button = tk.Button(root, text='Remove Task', command=remove_task)
remove_button.grid(row=2, column=3, padx=5, pady=10)

# Load tasks
tasks = load_tasks()
update_task_list()

root.mainloop()