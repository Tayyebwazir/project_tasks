import os

# Define the file where tasks will be stored
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def list_tasks(tasks):
    """List all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks, task):
    """Add a new task."""
    tasks.append(task)
    save_tasks(tasks)

def remove_task(tasks, task_number):
    """Remove a task by its number."""
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '3':
            list_tasks(tasks)
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(tasks, task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
