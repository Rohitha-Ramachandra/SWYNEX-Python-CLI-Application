def get_choice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Please enter a number.")
        return None


def get_task_number():
    try:
        number = int(input("Enter task number: "))
        return number
    except ValueError:
        print("Please enter a valid task number.")
        return None