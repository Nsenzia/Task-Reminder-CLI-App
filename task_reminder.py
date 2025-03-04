import sys

TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added: "{task}"')

def list_tasks():
    tasks = load_tasks()
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found!")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task removed: "{removed_task}"')
    else:
        print("Invalid task number!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python task_reminder.py add 'Task description'")
        print("  python task_reminder.py list")
        print("  python task_reminder.py delete <task_number>")
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))
    else:
        print("Invalid command!")
