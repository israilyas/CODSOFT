from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Treeview")
root.geometry("500x500")

my_TW = ttk.Treeview(root)

#Define ou columns in tuple
my_TW['column'] = ("Title", "Description", "Due Date")

#fomate columns
my_TW.column("#0",width=120, minwidth=25)
my_TW.column("Title", anchor=W,width=120, minwidth=25)
my_TW.column("Description",anchor=CENTER, width=120, minwidth=25)
my_TW.column("Due Date",anchor=W, width=120, minwidth=25)

# Create Headings
my_TW.heading("#0",text="Label")
my_TW.heading("Title",text="Title", anchor=W)
my_TW.heading("Description",text="Description", anchor=CENTER)
my_TW.heading("Due Date",text="Due Date", anchor=W)

#ADD DATA
my_TW.insert(parent='', index='end', iid=0, text="Parent", values=("coding","code for gui development","23-March"))
my_TW.insert(parent='', index='end', iid=1, text="Parent", values=("coding","code for gui development","23-March"))
my_TW.insert(parent='', index='end', iid=2, text="Parent", values=("coding","code for gui development","23-March"))
my_TW.insert(parent='', index='end', iid=3, text="Parent", values=("coding","code for gui development","23-March"))
my_TW.insert(parent='', index='end', iid=4, text="Parent", values=("coding","code for gui development","23-March"))
my_TW.insert(parent='', index='end', iid=5, text="Parent", values=("coding","code for gui development","23-March"))
my_TW.insert(parent='', index='end', iid=6, text="Parent", values=("coding","code for gui development","23-March"))

#Pack to screen
my_TW.pack(pady=10)

root.mainloop()