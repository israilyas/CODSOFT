tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added successfully")

def view_task():
    if len(tasks)==0:
        print("No task is added!")
    else:
        print("List of tasks:")  
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")  

def delete_task():
    if len(tasks)==0:
        print("No tasks to delete.")            
    else:
        print("Tasks: ")  
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")  
        choice = int(input("Enter the task number to delete:"))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

def main():
    while True:
        print("\n==== To-Do_List Application ====")
        print("1. Add Task\n2. View Task\n3. Delete Task\n4. Quit")

        user_choice = int(input("Enter your choice:"))
        if user_choice==1:
            add_task()
        elif user_choice==2:
            view_task()    
        elif user_choice==3:
            delete_task()    
        elif user_choice==4:
            print("Exiting...")
            quit()   
        else:
            print("Enter a valid choice")    

if __name__=="__main__":
    main()








