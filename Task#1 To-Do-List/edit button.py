import tkinter as tk
from tkinter import simpledialog

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.tasks = []

        self.task_frame = tk.Frame(self.master)
        self.task_frame.pack()

        self.edit_button = tk.Button(self.task_frame, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

    def edit_task(self):
        if not self.tasks:
            tk.messagebox.showinfo("Info", "No tasks available to edit.")
            return

        task_index = simpledialog.askinteger("Edit Task", "Enter task index to edit (starting from 1):", parent=self.master)
        if task_index is None or task_index <= 0 or task_index > len(self.tasks):
            tk.messagebox.showwarning("Warning", "Invalid task index.")
            return

        task = self.tasks[task_index - 1]
        new_title = simpledialog.askstring("Edit Task", "Enter new title:", parent=self.master, initialvalue=task.title)
        new_description = simpledialog.askstring("Edit Task", "Enter new description:", parent=self.master, initialvalue=task.description)
        new_due_date = simpledialog.askstring("Edit Task", "Enter new due date:", parent=self.master, initialvalue=task.due_date)

        # Update task with new information
        task.title = new_title
        task.description = new_description
        task.due_date = new_due_date

        tk.messagebox.showinfo("Info", "Task edited successfully.")

def main():
    root = tk.Tk()
    root.title("Task Manager")

    app = TaskManagerApp(root)

    root.mainloop()

if __name__ == "__main__":
    main()
