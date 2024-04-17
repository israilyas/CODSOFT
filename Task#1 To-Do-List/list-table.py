# import tkinter as tk
# from tkinter import ttk

# def add_task():
#     title = entry_title.get()
#     description = text_description.get("1.0", "end-1c")
#     due_date = entry_due_date.get()
    
#     listbox_tasks.insert("", "end", values=(title, description, due_date))
    
#     entry_title.delete(0, tk.END)
#     text_description.delete("1.0", tk.END)
#     entry_due_date.delete(0, tk.END)

# root = tk.Tk()
# root.title("Task Manager")

# frame_tasks = tk.Frame(root)
# frame_tasks.pack()

# columns = ("Title", "Description", "Due Date")
# listbox_tasks = ttk.Treeview(frame_tasks, columns=columns, show="headings")
# for col in columns:
#     listbox_tasks.heading(col, text=col)
# listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=listbox_tasks.yview)
# scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
# listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

# frame_input = tk.Frame(root)
# frame_input.pack()

# label_title = tk.Label(frame_input, text="Title:")
# label_title.grid(row=0, column=0, padx=5, pady=5)

# entry_title = tk.Entry(frame_input, width=30)
# entry_title.grid(row=0, column=1, padx=5, pady=5)

# label_description = tk.Label(frame_input, text="Description:")
# label_description.grid(row=1, column=0, padx=5, pady=5)

# text_description = tk.Text(frame_input, width=30, height=5)
# text_description.grid(row=1, column=1, padx=5, pady=5)

# label_due_date = tk.Label(frame_input, text="Due Date:")
# label_due_date.grid(row=2, column=0, padx=5, pady=5)

# entry_due_date = tk.Entry(frame_input, width=30)
# entry_due_date.grid(row=2, column=1, padx=5, pady=5)

# button_add_task = tk.Button(frame_input, text="Add Task", width=48, command=add_task)
# button_add_task.grid(row=3, columnspan=2, padx=5, pady=5)

# root.mainloop()

import tkinter as tk
from tkinter import ttk

def add_task():
    title = entry_title.get()
    description = text_description.get("1.0", "end-1c")
    due_date = entry_due_date.get()
    
    listbox_tasks.insert("", "end", values=(title, description, due_date))
    
    entry_title.delete(0, tk.END)
    text_description.delete("1.0", tk.END)
    entry_due_date.delete(0, tk.END)

root = tk.Tk()
root.title("Task Manager")

frame_tasks = tk.Frame(root)
frame_tasks.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.6)

columns = ("Title", "Description", "Due Date")
listbox_tasks = ttk.Treeview(frame_tasks, columns=columns, show="headings")
for col in columns:
    listbox_tasks.heading(col, text=col)
    listbox_tasks.column(col, anchor="center")  # Aligning text in the center of each column
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

frame_input = tk.Frame(root)
frame_input.place(relx=0.02, rely=0.65, relwidth=0.96, relheight=0.33)

label_title = tk.Label(frame_input, text="Title:")
label_title.place(relx=0.05, rely=0.05)

entry_title = tk.Entry(frame_input, width=30, justify="center")
entry_title.place(relx=0.3, rely=0.05)

label_description = tk.Label(frame_input, text="Description:")
label_description.place(relx=0.05, rely=0.25)

text_description = tk.Text(frame_input, width=30, height=5)
text_description.place(relx=0.3, rely=0.25)

label_due_date = tk.Label(frame_input, text="Due Date:")
label_due_date.place(relx=0.05, rely=0.65)

entry_due_date = tk.Entry(frame_input, width=30, justify="center")
entry_due_date.place(relx=0.3, rely=0.65)

button_add_task = tk.Button(frame_input, text="Add Task", width=48, command=add_task)
button_add_task.place(relx=0.05, rely=0.85, relwidth=0.9)

root.mainloop()



