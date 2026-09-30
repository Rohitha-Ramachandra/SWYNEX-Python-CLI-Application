tasks = []


def add_task(title):
    if not title.strip():
        raise ValueError("Task cannot be empty.")

    task = {
        "title": title.strip(),
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['title']} - {status}")


def complete_task(task_number):
    if task_number < 1 or task_number > len(tasks):
        raise IndexError("Invalid task number.")

    tasks[task_number - 1]["completed"] = True
    print("Task completed successfully.")


def delete_task(task_number):
    if task_number < 1 or task_number > len(tasks):
        raise IndexError("Invalid task number.")

    tasks.pop(task_number - 1)
    print("Task deleted successfully.")