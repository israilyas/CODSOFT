# import tkinter as tk

# def add_task():
#     task = entry_task.get()
#     if task:
#         listbox_tasks.insert(tk.END, task)
#         entry_task.delete(0, tk.END)

# def delete_task():
#     try:
#         task_index = listbox_tasks.curselection()[0]
#         listbox_tasks.delete(task_index)
#     except IndexError:
#         pass

# root = tk.Tk()
# root.title("Task Manager")

# frame_tasks = tk.Frame(root)
# frame_tasks.pack()

# listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
# listbox_tasks.pack(side=tk.LEFT)

# scrollbar_tasks = tk.Scrollbar(frame_tasks)
# scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
# scrollbar_tasks.config(command=listbox_tasks.yview)

# entry_task = tk.Entry(root, width=50)
# entry_task.pack()

# button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
# button_add_task.pack()

# button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
# button_delete_task.pack()

# root.mainloop()


import tkinter as tk

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
        save_tasks()
    except IndexError:
        pass

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

root = tk.Tk()
root.title("Task Manager")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

load_tasks()  # Load tasks when the application starts

root.mainloop()

