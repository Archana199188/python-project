tasks = []

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added!")

def delete_task():
    show_tasks()
    task_no = int(input("Enter task number to delete: "))
    if 0 < task_no <= len(tasks):
        tasks.pop(task_no - 1)
        save_tasks()
        print("Task deleted!")
    else:
        print("Invalid task number")

# Load tasks when program starts
load_tasks()

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice")