to_do_list = []

def add_task(to_do_list):
    task = input("Choice to-do task: ")
    to_do_list.append(task)
    print("Task added succesfuly")

def show_tasks(to_do_list):
    print("To-do Tasks: ")
    for task in to_do_list:
        print("- "+ task)

def delete_task(to_do_list):
    task = input("Delete task: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print("Task deleted.")
    else:
        print("Task not found")

while True:
    print("\nTo-Do List App")
    print("1- Add Task")
    print("2- Show Tasks")
    print("3- Delete Task")
    print("4- Exit")
    choice = input("Choice : (1-2-3-4): ")
    
    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_tasks(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("Power off...")
        break
    else:
        print("Invalid Choice")
