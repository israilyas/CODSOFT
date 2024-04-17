import string
import random
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())

    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbolD = string.punctuation

    combine = lowerD + upperD + digitD + symbolD

    try:
        password = "".join(random.sample(combine, length))
        password_display.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Password length cannot exceed the available character set length.")

# Function to stop generating passwords
def stop_generating():
    root.quit()
    
# Color theme
background = "#0D1B2A"
buttons = "#3F88C5"
buttonfg = "white"
labelfg = "white"

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("450x350+220+100")
root.config(bg=background)

#------- GUI components----------

label = tk.Label(text="RANDOM PASSWORD GENERATOR" ,font="arial 12 bold",bg=background,fg=labelfg)
label.place(relx=0.2, rely=0.15)

length_label = tk.Label(root, text="length of password:" ,font="arial 12",bg=background,fg=buttonfg )
length_label.place(relx=0.15, rely=0.35)

length_entry = tk.Entry(root )
length_entry.place(relx=0.5, rely=0.36)

generate_button = tk.Button(root, text="Generate", command=generate_password ,bg=buttons , font="Arial 12" ,relief="raised",fg=buttonfg)
generate_button.place(relx=0.4, rely=0.47)

password_display = tk.Label(root, text="",font="Arial 12",bg=background, fg=buttonfg)
password_display.place(relx=0.2, rely=0.6)

root.mainloop()
