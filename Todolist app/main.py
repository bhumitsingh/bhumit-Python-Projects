import json

# File to store tasks
tasks_file = 'tasks.json'

# Load tasks from file
def load_tasks():
    try:
        with open(tasks_file, 'r') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return []
    
# Save tasks to file
def save_tasks(tasks):
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f'Task "{task}" added')

# List all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found')
        return
    for idx, task in enumerate(tasks, start=1):
        status = 'Done' if task['done'] else 'Not done'
        print(f"{idx}. {status} : {task['task']}")

# Mark a task as done
def mark_done(index):
    tasks = load_tasks()
    if 0<index<=len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f'Task {index} marked as done')
    else:
        print('Invalid task number')

# Remove a task
def remove_task(index):
    tasks = load_tasks()
    if 0<index<=len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f'Task "{removed["task"]}" removed')
    else:
        print('Invalid task number')
def main():
    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            index = int(input("Enter task number to mark as done: "))
            mark_done(index)
        elif choice == '4':
            view_tasks()
            index = int(input("Enter task number to remove: "))
            remove_task(index)
        elif choice == '5':
            print('Exiting...')
            break
        else:
            print('Invalid choice')
if __name__ == '__main__':
    main()
