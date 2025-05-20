
tasks = []

def add_task(title, description):
    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully.")

def update_task(index, title, description):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = title
        tasks[index]["description"] = description
        print("Task updated successfully.")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

def mark_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def display_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {task['description']} [{status}]")

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Display All Tasks")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == 2:
            display_tasks()
            index = int(input("Enter task index to update: "))
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            update_task(index, title, description)
        elif choice == 3:
            display_tasks()
            index = int(input("Enter task index to delete: "))
            delete_task(index)
        elif choice == 4:
            display_tasks()
            index = int(input("Enter task index to mark as completed: "))
            mark_completed(index)
        elif choice == 5:
            display_tasks()
        elif choice == 6:
            print("Exiting Task Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
