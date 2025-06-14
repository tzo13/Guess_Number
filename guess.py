import tkinter as tk
from tkinter import ttk
import random

def create_purple_theme(screen, mpla, easy, medium, hard, keimeno, entry, btn_exit, btn_random):
    # Set the background and text color for the root window
    screen.configure(bg="#5851db")  # Purple background for the screen

    # Manually styling buttons
    btn_style = {
        "bg": "#5d7eba",  # Purple background
        "fg": "white",  # White text
        "bd": 0,
        "relief": "flat",
        "padx": 10,
        "pady": 5
    }

    # Manually styling labels
    label_style = {
        "bg": "#5191db",  # Lavender background
        "fg": "#6a0dad",  # Purple text
        "font": ("Arial", 12)
    }

    # Manually styling entry fields
    entry_style = {
        "bg": "#f0f0f0",
        "fg": "#6a0dad",
        "bd": 1
    }

    # Apply styles to widgets directly
    mpla.config(label_style)
    easy.config(btn_style)
    medium.config(btn_style)
    hard.config(btn_style)
    keimeno.config(label_style)
    entry.config(entry_style)
    btn_exit.config(btn_style)
    btn_random.config(btn_style)

# Set up the main window
screen = tk.Tk()
screen.title("Purple Themed Interface")

# Define a variable to hold the selected difficulty
difficulty = tk.IntVar()
difficulty.set(2)
tries = 0
up = tk.PhotoImage(file = "uparrow.png")
down = tk.PhotoImage(file = "downarrow.png")
check = tk.PhotoImage(file = "correct.png")
zari= tk.PhotoImage(file = "dice1.png")




def rand():
    global difficulty,x
    diff = difficulty.get()
    if diff == 1:
        x = random.randint(0, 50)
    elif diff == 2:
        x = random.randint(0, 400)
    elif diff ==3:
        x = random.randint(0,1000)
    print(x)


def checka(event):
    global x,tries
    a = int(entry.get())

    if a > x:
        img.configure(image = down)
        tries += 1
    elif a <x:
        img.configure(image = up)
        tries += 1
    elif a == x:
        img.configure(image = check)
        tries = 0
    triess.configure(text="Tries:"+ str(tries))
    entry.delete(0,1000)


# Create and place widgets on the screen
mpla = tk.Label(screen, text="Guess the number!")
easy = tk.Radiobutton(screen, text="Easy 0 - 50", value=1, variable=difficulty)
medium = tk.Radiobutton(screen, text="Medium 0 - 100", value=2, variable=difficulty)
hard = tk.Radiobutton(screen, text="Hard 0 - 200", value=3, variable=difficulty)
keimeno = tk.Label(screen, text="Start the game by guessing a number!")
img = tk.Label(screen,image = zari)
entry = tk.Entry(screen)
btn_exit = tk.Button(screen, text="EXIT", command=screen.quit)
btn_random = tk.Button(screen, text="Random Number",command = rand)  # Button for random number functionality
triess = tk.Label(screen, text = "Tries: ")




# Arrange the widgets in the grid layout
mpla.grid(row=0, column=0, columnspan=3, pady=10)
easy.grid(row=1, column=0)
medium.grid(row=1, column=1)
hard.grid(row=1, column=2)
keimeno.grid(row=2, column=0, columnspan=3, pady=10)
img.grid(row=3, column=0, padx=10)
entry.grid(row=3, column=1, padx=10)
btn_exit.grid(row=3, column=2)
btn_random.grid(row=4, column=2)
triess.grid(row =5, column = 1)

# Apply the purple theme by passing widgets to the function
create_purple_theme(screen, mpla, easy, medium, hard, keimeno, entry, btn_exit, btn_random)
screen.bind('<Return>',checka)
# Start the Tkinter event loop
screen.mainloop()
