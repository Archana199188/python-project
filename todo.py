tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    task_no = int(input("Enter task number to delete: "))
    if 0 < task_no <= len(tasks):
        tasks.pop(task_no - 1)
        print("Task deleted!")
    else:
        print("Invalid task number")

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