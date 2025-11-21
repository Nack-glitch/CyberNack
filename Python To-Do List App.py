tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Edit Task")
    print("6. Clear All Tasks")
    print("7. Exit")

def add_task():
    new_tasks = input("Enter task(s) separated by comma: ").split(",")
    for task in new_tasks:
        task = task.strip()
        if task:
            tasks.append({"task": task, "done": False})
            print(f'Task "{task}" added!')

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔ Done" if task["done"] else "❌ Not done"
            print(f"{i}. {task['task']} - {status}")

def remove_task():
    view_tasks()
    if tasks:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f'Task "{removed["task"]}" removed!')
        else:
            print("Invalid number!")

def mark_done():
    view_tasks()
    if tasks:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f'Task "{tasks[task_num - 1]["task"]}" marked as done!')
        else:
            print("Invalid number!")

def edit_task():
    view_tasks()
    if tasks:
        task_num = int(input("Enter task number to edit: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter new task description: ").strip()
            if new_task:
                tasks[task_num - 1]["task"] = new_task
                print("Task updated!")
        else:
            print("Invalid number!")

def clear_tasks():
    tasks.clear()
    print("All tasks cleared!")

while True:
    show_menu()
    choice = input("Choose an option (1-7): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        edit_task()
    elif choice == "6":
        clear_tasks()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again!")
