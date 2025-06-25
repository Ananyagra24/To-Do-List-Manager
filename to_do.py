filename = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

    return tasks

def save_tasks(tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nYour tasks:")
        id = 1
        for task in tasks:
            print(f"{id}.{task}")
            id = id + 1
        print()

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.\n")
        view_tasks(tasks)
    else:
        print("Task cannot be empty.\n")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter the number to remove: ").strip())
            if 1 <= num <= len(tasks):
                confirm = input(f"Are you sure you want to delete task no.{num}? (y/n): ").strip()
                if confirm.lower() == "y":
                    removed = tasks.pop(num-1)
                    save_tasks(tasks)
                    print(f"Removed task: {removed}\n")
                else:
                    print("Invalid confirmation.\n")
            else:
                print("Invalid task number. \n")
        except ValueError:
            print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("To-Do List Manager \n")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        match choice:
            case '1':
                view_tasks(tasks)
            case '2':
                add_task(tasks)
            case '3':
                remove_task(tasks)
            case '4':
                print("Exiting To-Do List Manager")
                break
            case _:
                print("Invalid choice. Please try again. \n")

if __name__ == "__main__":
    main()