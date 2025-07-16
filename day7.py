import os

text_file = "tasks.txt"

def load_tasks():
    tasks = []

    if(os.path.exists(text_file)):
        with open (text_file , 'r' , encoding = "utf-8") as f:
            for line in f:
                text , status = line.strip().rsplit("||" , 1) # one splitting from the right and will split when it encounters "||"
                tasks.apppend({"text" : text, "done" : status == "done"})

    return tasks

def save_tasks(tasks):
    with open(text_file , "w" , encoding = "utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task["text"]} || {status}\n")

def display_tasks(tasks):
    if not tasks:
        print("tasks are yet to be added!")
    else:
        for i,task in enumerate(tasks , 1): #enumerate is used for numbering of tasks in this case
            checkbox = "✔" if task["done"] else "❌"
            print(f"{i}: {task["text"]} {checkbox}")

    print()

def task_manager():
    tasks = load_tasks()

    while True:
        print("\n\t\tTask Manager\n")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Update task status")
        print("4. Delete task")
        print("5. Exit")

        choice = int(input("enter your choice: "))

        match choice:
            case 1:
                text = input("enter your task to add: ").strip()

                if text:
                    tasks.append({"text" : text , "done" : False})
                    save_tasks(tasks)
                else:
                    print("invalid task")

            case 2:
                display_tasks(tasks)

            case 3:
                display_tasks(tasks)

                try:
                    update = int(input("enter task number to be updated: "))

                    if update >=1 and update <= len(tasks):
                        tasks[update-1]["done"] = True
                        save_tasks(tasks)
                        print("task status updated!")

                    else:
                        print("invalid value of task")
                
                except ValueError:
                    print("Please enter a valid number")

            case 4:
                display_tasks(tasks)

                try:
                    delete = int(input("enter task number to delete: "))

                    if delete >=1 and delete <= len(tasks):
                        removed = tasks.pop(delete-1)

                        print(f"task removed {removed["text"]}")
                    else:
                        print("invalid value of task")
                
                except ValueError:
                    print("Please enter a valid number")

            case 5:
                print("Thanks for using this!")
                break

            case _:
                print("invalid choice/option!\n\n")

task_manager()