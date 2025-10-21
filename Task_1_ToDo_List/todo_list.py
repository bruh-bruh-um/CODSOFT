import os

TASKS_FILE = "tasks.txt"

# Load tasks from file (if exists)
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "done": status == "Done"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for t in tasks:
            status = "Done" if t["done"] else "Pending"
            file.write(f"{t['task']} | {status}\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n No tasks yet!")
        return
    print("\n Your Tasks:")
    for i, t in enumerate(tasks, 1):
        status = " if t["done"] else "
        print(f"{i}. {t['task']} [{status}]")

# Add new task
def add_task(tasks):
    task = input("\nEnter new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("Task added successfully!")

# Mark task as done
def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nEnter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(" Task marked as done!")
        else:
            print(" Invalid number.")
    except ValueError:
        print(" Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"️ Deleted task: {removed['task']}")
        else:
            print(" Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\n TO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print(" Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
