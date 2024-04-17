from tkinter import *
import random

# MAIN PROGRAMME
choices = ['rock', 'scissor', 'paper']

# GUI
root = Tk()
root.geometry("655x455+200+100")
root.title("Rock Paper Scissor")

# Color theme
primary_color = "#C1CDC1"
secondary_color = "#6A90B6"
accent_color = "#FF6B35"
text_color = "black"

root.config(bg=primary_color)

rock_image = PhotoImage(file="asset/icons8-hand-rock-50.png")
paper_image = PhotoImage(file="asset/icons8-hand-50.png")
scissor_image = PhotoImage(file="asset/icons8-hand-scissors-50.png")

Variable = StringVar()


def tab1():
    def result_tab(user_choice):
        label1.destroy()
        label2.destroy()
        rock_button.destroy()
        paper_button.destroy()
        scissor_button.destroy()
        rock_lab.destroy()
        paper_lab.destroy()
        scissor_lab.destroy()

        computer_choice = random.choice(choices)
        computer_label = Label(root, text="Computer Choice", font="arial 12", bg=primary_color, fg=text_color, relief=RIDGE, padx=7, pady=7)
        computer_label.place(x=130, y=70)
        computer_img = Label(root, image=computer_choice_image[computer_choice], padx=20, width=60, height=60,)  # Fix here
        computer_img.place(x=160, y=150)

        user_label = Label(root, text="Your Choice", font="arial 12", bg=primary_color, fg=text_color, relief=RIDGE, padx=18, pady=7)
        user_label.place(x=380, y=70)
        img_label = Label(root, image=user_choice_image[user_choice], padx=20, width=60, height=60)
        img_label.place(x=410, y=150)

        result_frame = Frame(root, width=330, height=100, bg="black")
        result_frame.place(x=150, y=250)

        lab = Label(result_frame, text="RESULT", fg="white" , bg="black", font="arial 13")
        lab.place(x=130, y=10)

        result_label = Label(result_frame, text="", font="arial 13 bold", wraplength=300, justify="center", bg="black", fg="white")
        result_label.place(x=10, y=40)


        if user_choice == computer_choice:
            result_label.config(text="It's a tie!")

        elif (
            (user_choice == 'rock' and computer_choice == 'scissor') or
            (user_choice == 'scissor' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            result_label.config(text="Congratulations! You have won")

        else:
            result_label.config(text="Computer wins!")

        def back():
            user_label.destroy()
            img_label.destroy()
            computer_label.destroy()  
            computer_img.destroy()     
            result_label.destroy()
            back_button.destroy()
            result_frame.destroy()
            lab.destroy()
            tab1()

        back_button = Button(text="BACK", command=back, font="arial 13 ")
        back_button.place(x=300, y=400)

    user_choice_image = {
        'rock': rock_image,
        'scissor': scissor_image,
        'paper': paper_image
    }

    computer_choice_image = {
        'rock': rock_image,
        'scissor': scissor_image,
        'paper': paper_image
    }

    label1 = Label(root, text="Rock-Paper-Scissor Game", font="arial 20 bold", bg=primary_color, fg=text_color, width=20)
    label1.place(x=170, y=60)

    label2 = Label(root, text="Make your choice", font="arial 13 ", bg=primary_color, fg=text_color, width=20, relief=RIDGE, padx=5, pady=5)
    label2.place(x=240, y=150)

    rock_button = Button(root, image=rock_image, padx=20, width=60, height=60, command=lambda: result_tab('rock'))
    rock_button.place(x=210, y=220)

    rock_lab = Label(root, text="ROCK", bg=primary_color, font="arial 9")
    rock_lab.place(x=220, y=300)

    paper_button = Button(root, image=paper_image, padx=20, width=60, height=60, command=lambda: result_tab('paper'))
    paper_button.place(x=300, y=220)

    paper_lab = Label(root, text="PAPER", bg=primary_color, font="arial 9")
    paper_lab.place(x=310, y=300)

    scissor_button = Button(root, image=scissor_image, padx=20, width=60, height=60, command=lambda: result_tab('scissor'))
    scissor_button.place(x=390, y=220)

    scissor_lab = Label(root, text="SCISSOR", bg=primary_color, font="arial 9")
    scissor_lab.place(x=390, y=300)

# Call the initial tab setup
tab1()

root.mainloop()
