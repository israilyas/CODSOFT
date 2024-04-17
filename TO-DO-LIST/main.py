from tkinter import *
from tkinter import ttk
import ttkbootstrap as tb
from tkcalendar import *
import openpyxl
from openpyxl import load_workbook
from openpyxl.workbook import Workbook

combo_list = ["Subscribed","Not subscribed","Other"]



root = Tk()
# root.geometry("600x400")
style = ttk.Style(root)
# root.tk.call("source","forest-dark.tcl")
# root.tk.call("source","forest-light.tcl")
# style.theme_use("forest-dark")


frame = ttk.Frame(root)
frame.pack()

widget_frame = ttk.LabelFrame(frame,text="Add Task")
widget_frame.grid(row=0,column=0, padx=20, pady=25)

title_entry = ttk.Entry(widget_frame ,width=40)
title_entry.insert("0","Title")
title_entry.bind("<FocusIn>", lambda dlt: title_entry.delete("0",END))
title_entry.grid(row=0, column=0, sticky="ew", padx=10, pady=(10,5))

date_entry = tb.DateEntry(widget_frame, bootstyle="success",width=40)
date_entry.grid(row=1, column=0, sticky="ew", padx=10, pady=(0,5))

age_spinbox = ttk.Spinbox(widget_frame, from_=10, to=100,width=40)
age_spinbox.insert("0","Age")
age_spinbox.bind("<FocusIn>", lambda dlt: age_spinbox.delete("0",END))
age_spinbox.grid(row=2, column=0, sticky="ew", padx=10, pady=(0,5))

status_combobox = ttk.Combobox(widget_frame, values=combo_list,width=40)
status_combobox.current(0)
status_combobox.grid(row=3, column=0, sticky="ew", padx=10, pady=(0,5))

a = BooleanVar()
checkbutton = ttk.Checkbutton(widget_frame, text="Employed", variable=a)
checkbutton.grid(row=4, column=0, sticky="nsew", padx=10, pady=(10,10))

button = ttk.Button(widget_frame, text="Insert",width=40)
button.grid(row=5, column=0, sticky="nsew", padx=10, pady=(0,5))

separator = ttk.Separator(widget_frame)
separator.grid(row=6, column=0, padx=(20,10), pady=10, sticky="ew")

# mode_switch = ttk.Checkbutton(widget_frame, text="Mode" , style="Switch.TButton", width=40)
# mode_switch.grid(row=7,column=0, padx=10, pady=10, sticky="nsew")


# TREEVIEW
treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side=RIGHT, fill=Y)

cols =("Name","Age","Subscription","Emplayement")
treeview = ttk.Treeview(treeFrame, show="headings", columns=cols, height=13, yscrollcommand=treeScroll.set)

treeview.column("Name", width=100)
treeview.column("Age", width=50)
treeview.column("Subscription", width=100)
treeview.column("Emplayement", width=100)

# Create Headings
treeview.heading("Name",text="Name")
treeview.heading("Age",text="Age", anchor=W)
treeview.heading("Subscription",text="Subscription", anchor=CENTER)
treeview.heading("Emplayement",text="Emplayement", anchor=W)


treeview.pack()
treeScroll.config(command=treeview.yview)

# load_data()


root.mainloop()


