
print("==== TO DO LIST APPLICATION === \n1. Add Task \n2. Delete Tasks \n3. View Tasks \n4. Quit" )
task_list = []

def add_task():
     add_task = input("Enter a new task: ")
     task_list.append(add_task)
     print("Task added successfully")

def view_task():
    print("Here is the list of tasks:")
    for index,task in enumerate(task_list):
        print(f"{index+1}: {task} ")
def delete_task():
     if len(task_list)<=0:
            print("No task is available")
     else:
        print("Here is the list of tasks:")
        for index,task in enumerate(task_list , start=1):
           print(f"{index}: {task}")
        dlt_index = int(input("Please enter a task number which you want to delete!"))
        if  0 < dlt_index <= len(task_list):
            del task_list[dlt_index-1]
            print("Task is deleted Successfully!")
        else:
            print("Please enter a valid number!")

while True:
    choice = int(input("Enter your choice "))
    if choice == 1:
        add_task()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        view_task()
    elif choice == 4:
        quit()
    else:
        print("Enter a valid choice!")
