



from tasks import add_task, view_tasks, complete_task, delete_task
from utils import get_choice, get_task_number


def main():
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = get_choice()

        if choice == 1:
            title = input("Enter task title: ")
            try:
                add_task(title)
            except ValueError as error:
                print(error)

        elif choice == 2:
            view_tasks()

        elif choice == 3:
            number = get_task_number()
            if number is not None:
                try:
                    complete_task(number)
                except IndexError as error:
                    print(error)

        elif choice == 4:
            number = get_task_number()
            if number is not None:
                try:
                    delete_task(number)
                except IndexError as error:
                    print(error)

        elif choice == 5:
            print("Thank you for using Task Manager!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()