from tkinter import *


#FUNCTIONS
def add_task():
    pass
  
def view_tasks():
    pass

def upcoming_task():
    pass

def help():
    pass

def edit_task():
    pass

def change_theme():
    pass

def submit_func():
    pass

#GUI LOGIC

root = Tk()
root.geometry("855x555")  # width x height

#color variables ---->

# Light Theme Colors
# bg_color_primary = "#f2f2f2"       # Light Gray
# bg_color_secondary = "#ccc"        # Light Gray (Secondary)
# bg_color_heading = "#333"          # Dark Gray
# bg_color_left_frame = "#666"       # Gray
# bg_color_right_frame = "#ff6666"   # Light Red
# fg_color_heading = "#fff"          # White
# fg_color_text = "#333"             # Dark Gray (Text)

# bg_color_primary = "#333"
# bg_color_secondary = "#666"
# bg_color_heading = "#ccc"
# bg_color_left_frame = "#999"
# bg_color_right_frame = "#ff3333"
# fg_color_heading = "#fff"
# fg_color_text = "#ccc"

bg_color_primary = "#0056b3"  # Dark Blue
bg_color_secondary = "#b3cde0"  # Light Blue
bg_color_heading = "#0056b3"          #"#333"  # Dark Gray
bg_color_left_frame = "#0056b3"       #"#666"  # Gray
bg_color_right_frame = "#ff6666"  # Light Red
fg_color_heading = "#fff"  # White
fg_color_text = "#333"  # Dark Gray
bg_right_fame_color = "#0056b3" 

root.config(bg=bg_color_secondary)  # Setting background color of the root window

lab = Label(text="Organize Your Tasks, Simplify Your Life", bg=bg_color_heading, fg=fg_color_heading, font=("Iskoola Pota", 15, "bold"), padx=15, pady=12)
lab.pack(fill="x")

def tab1():
    # Left Frame
    f1 = Frame(root, bg=bg_color_left_frame, borderwidth=2, relief=SUNKEN)
    f1.pack(side='left', fill="y")

    add_task_button = Button(f1,command=add_task, text="Add Task",padx=70)
    add_task_button.pack(fill="x")

    view_tasks_button = Button(f1,command=view_tasks, text="View All Tasks")
    view_tasks_button.pack(fill="x")

    edit_task_button = Button(f1,command=edit_task, text="Update Task")
    edit_task_button.pack(fill="x")

    upcoming_task_button = Button(f1,command=upcoming_task, text="Upcoming Task")
    upcoming_task_button.pack(fill="x")

    change_theme_button = Button(f1,command=change_theme, text="Change Theme")
    change_theme_button.pack(fill="x")

    help_button = Button(f1,command=help, text="Help")
    help_button.pack(fill="x")

    # Top Frame
    f2 = Frame(root, bg=bg_color_secondary, borderwidth=6, relief=SUNKEN)
    f2.pack(side="top", fill="x")

    l2 = Label(f2, text="Welcome to Your Task Manager", font=("Arial", 12, "bold"), fg=fg_color_text, bg=bg_color_secondary)
    l2.pack()

    # Right Frame
    f3 = Frame(root,  borderwidth=6, relief=SUNKEN, bg=bg_color_secondary)
    f3.pack(side="right", fill="both", expand=True)

    # ADD TASK FRAME
    add_task_frame = Frame(f3,borderwidth=6, relief="solid", bg=bg_right_fame_color)
    add_task_frame.pack(padx=(50,50),pady=100, expand=True)

    f3_label = Label(add_task_frame, text="Add Task:", font=("Arial", 12, "bold"), fg="white", bg=bg_right_fame_color)
    f3_label.pack(pady=10,padx=50)
    # add task entry
    task_entry = Entry(add_task_frame, )
    task_entry.pack(fill="x", padx=20, pady=3)
    # task details
    detail_label = Label(add_task_frame, text="Task Details", bg=bg_right_fame_color, font=("Arial", 12, "bold"), fg="white")
    detail_label.pack(pady=5)
    details_box = Text(add_task_frame)
    details_box.pack(padx=20, pady=2)
    #submit task button
    submit_task = Button(f1, text="Submit",command=submit_func , bg=bg_color_secondary)
    submit_task.pack()
    # submit_task = Button(ad, text="Submit",command=submit_func , bg=bg_color_secondary)
    # submit_task.pack()
    # Submit task 
    submit_task = Button(f3, text="Submit", command=submit_func, bg="black", fg="white")
    submit_task.pack()
    
tab1()

root.mainloop()
