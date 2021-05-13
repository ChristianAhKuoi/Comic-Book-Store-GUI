##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   CLASS CODE   ##########
class Comic:
    """This code will store the details of each comic (Super Dude, Lizard Man, Water Woman)"""
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
        comic_list.append(self)

##########   FUNCTION AND SETUP - COMIC WINDOW   ##########
# Functions...
def create_name_list():
  name_list = []
  for comic in comic_list:
    name_list.append(comic.name)
  return name_list

# Formatting Variables...
primary_color = "#38c8f5" #sky blue
secondary_color = "#e31679" #deep pink
tertiary_color = "#242424" #light black
accent_color = "#a6e5d0" #pale blue

# Setup Lists
comic_list = []

# Creating instances of comic class
super_dude = Comic("Super Dude", 8)
lizard_man = Comic("Lizard Man", 12)
water_woman = Comic("Water Woman", 3)
comic_names = create_name_list()

##########   COMIC GUI CODE   ##########
# Create a window with a title
root = Tk()
root.title("Comic Book Store")

# Set color of color window background
root.configure(bg="white")

# Comic frame
comic_frame = Frame(root, width=300, height=300, bg="white")
comic_frame.pack(padx=10, pady=5)

# Top frame
top_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
top_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Comic label - Heading (row 0, column 1)
comic_label = Label(top_frame,
                        text="Comic Book Store",
                        font=("Ariel", "16", "bold"),
                        bg=primary_color,
                        padx=150, pady=5
                        )
comic_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Left frame (row 2, column 0)
left_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
left_frame.grid(row=2, column=0, padx=10, pady=5)

# Summary label - (row 0, column 0)
summary_label = Label(left_frame,
                        text="Summary",
                        font=("Ariel", "16", "bold"),
                        bg=secondary_color,
                        padx=150, pady=5
                        )
summary_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Right frame (row 2, column 1)
right_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
right_frame.grid(row=2, column=1, padx=10, pady=5)

# Sell/Restock variables
mode_list = ['Sell', 'Restock']
chosen_mode = StringVar()
chosen_mode.set(mode_list[0])

# Sell/Restock label - (row 0, column 0)
mode_label = Label(right_frame,
                        textvariable=chosen_mode,
                        font=("Ariel", "16", "bold"),
                        bg=secondary_color,
                        padx=150, pady=5
                        )
mode_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Radiobutton LabelFrame - (row 1, column 0)
mode_label_frame = LabelFrame(right_frame)
mode_label_frame.grid(row=1, column=0, columnspan=2)

# Mode(Sell/Restock) Radiobutton
# Sell Radiobutton (row 0, column 0)
sell_radio = ttk.Radiobutton(mode_label_frame, text="Sell", value="sell"
                              )
sell_radio.grid(row=0, column=0, padx=10, pady=5)

# Restock Radiobutton (row 0, column 1)
sell_radio = ttk.Radiobutton(mode_label_frame, text="Restock", value="restock"
                              )
sell_radio.grid(row=0, column=1, padx=10, pady=5)

# Comic Combobox - (row 2, column 0)
# Setup variable and option list for the account Combobox
chosen_comic = StringVar()
chosen_comic.set(comic_names[0])

# Create a Combobox to select the comic
comic_combobox = ttk.Combobox(right_frame, textvariable=chosen_comic, state="readonly",
                              font=("Ariel", "12"),
                              width=20)
comic_combobox['values'] = comic_names
comic_combobox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main window loop
root.mainloop()
