##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   CLASS CODE   ##########
# Class code here...

##########   FUNCTION AND SETUP - COMIC WINDOW   ##########
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
root.configure(bg="white")

# Comic frame
comic_frame = Frame(root, width=300, height=300, bg="white")
comic_frame.pack(padx=10, pady=5)

# Top frame (row 0, column 0)
top_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Comic label - Heading (row 0, column 1)
comic_label = Label(top_frame,
                        text="Comic Book Store",
                        font=("Ariel", "16", "bold"),
                        bg=primary_color,
                        padx=150, pady=5
                        )
comic_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Left frame (row 1, column 0)
left_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
left_frame.grid(row=1, column=0, padx=10, pady=5)

# Summary label - (row 0, column 0)
summary_label = Label(left_frame,
                        text="Summary",
                        font=("Ariel", "16", "bold"),
                        bg=secondary_color,
                        width=22,
                        padx=10, pady=5
                        )
summary_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Right frame (row 1, column 1)
right_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
right_frame.grid(row=1, column=1, padx=10, pady=5)

# Sell/Restock variables
mode_list = ['Sell', 'Restock']
chosen_mode = StringVar()
chosen_mode.set(mode_list[0])

# Stock Manager label - (row 0, column 0)
stock_manager_label = Label(right_frame,
                        text="Stock Manager",
                        font=("Ariel", "16", "bold"),
                        width=22,
                        bg=secondary_color,
                        padx=10, pady=5
                        )
stock_manager_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Run the main window loop
root.mainloop()
