##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   CLASS CODE   ##########
class Comic:
    """This code will store the details of each comic (Super Dude, Lizard Man, Water Woman)"""
    def __init__(self, title, stock):
        self.title = title
        self.stock = stock

##########   FUNCTION AND SETUP - COMIC WINDOW   ##########
# Functions...

# Formatting Variables...
primary_color = "#38c8f5" #sky blue
secondary_color = "#e31679" #deep pink
tertiary_color = "#242424" #light black
accent_color = "#a6e5d0" #pale blue

##########   COMIC GUI CODE   ##########
# Create a window with a title
root = Tk()
root.title("Comic Book Store")

# Set color of color window background
root.configure(bg=tertiary_color)

# Comic frame
comic_frame = Frame(root, width=300, height=300, bg=tertiary_color)
comic_frame.grid(row=0, column=0, padx=10, pady=5)

# Comic label - Heading (row 0, column 1)
comic_label = Label(comic_frame,
                        text="Comic Book Store",
                        font=("Ariel", "16", "bold"),
                        bg=primary_color,
                        padx=150, pady=5
                        )
comic_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Left frame (row 1, column 0)
left_frame = Frame(comic_frame, width=300, height=250, bg=accent_color)
left_frame.grid(row=1, column=0, padx=10, pady=5)

# Right frame (row 1, column 1)
left_frame = Frame(comic_frame, width=300, height=250, bg=accent_color)
left_frame.grid(row=1, column=1, padx=10, pady=5)

# Run the main window loop
root.mainloop()
