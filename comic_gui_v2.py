##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   FUNCTION AND SETUP - COMIC WINDOW   ##########
# Functions...
def printy():
    print(mode_var.get())

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

# Comic label - Heading (row 0, column 0)
comic_label = Label(top_frame,
                        text="Comic Book Store",
                        font=("Ariel", "16", "bold"),
                        bg=primary_color,
                        padx=150, pady=5
                        )
comic_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

# Left frame (row 1, column 0)
left_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
left_frame.grid(row=1, column=0, padx=10, pady=5, sticky="NS")

# Summary label - (row 0, column 0)
summary_label = Label(left_frame,
                        text="Stock Summary",
                        font=("Ariel", "16", "bold"),
                        width=22,
                        bg=secondary_color,
                        padx=10, pady=5
                        )
summary_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

# Create and set comic details
comic_details = StringVar()
comic_details.set("Comics in stock: \n"
                  "Super Dude: 8 \n"
                  "Lizard Man: 12 \n"
                  "Water Woman: 3 \n\n"
                  "Total Sold: 0")

# Stock Details label - (row 1, column 0)
details_label = Label(left_frame, textvariable=comic_details,
                      font=("Ariel", "12", "bold"),
                      bg=accent_color, padx=10, pady=5
                      )
details_label.grid(row=1, column=0, columnspan=1, padx=10, pady=5)

# Right frame (row 1, column 1)
right_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
right_frame.grid(row=1, column=1, padx=10, pady=5, sticky="NS")

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

# Mode label - (row 1, column 0)
mode_label = Label(right_frame,
                        text="Mode:",
                        font=("Ariel", "12", "bold"),
                        bg=accent_color,
                        pady=2
                        )
mode_label.grid(row=1, column=0, padx=10, pady=5, sticky="WE")

# Radiobutton LabelFrame - (row 1, column 1)
mode_label_frame = LabelFrame(right_frame, bd=0)
mode_label_frame.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="W")

# Mode(Sell/Restock) Radiobutton
mode_var = StringVar()
mode_var.set("sell")

# Sell Radiobutton (row 0, column 0)
sell_radio = ttk.Radiobutton(mode_label_frame, text="Sell",
                             value="sell", variable=mode_var
                              )
sell_radio.grid(row=0, column=0, padx=10, pady=2)

# Restock Radiobutton (row 0, column 1)
restock_radio = ttk.Radiobutton(mode_label_frame, text="Restock",
                                value="restock", variable=mode_var
                              )
restock_radio.grid(row=0, column=1, padx=10, pady=2)

# Comic Combobox label - (row 2, column 0)
comic_combobox_label = Label(right_frame,
                        text="Comic:",
                        font=("Ariel", "12", "bold"),
                        bg=accent_color,
                        padx=10, pady=2
                        )
comic_combobox_label.grid(row=2, column=0, columnspan=1, padx=10, pady=5, sticky="WE")

# Comic Combobox
# Setup variable and option list for the account Combobox
comic_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_comic = StringVar()
chosen_comic.set(comic_names[0])

# Create a Combobox to select the comic - (row 2, column 1)
comic_combobox = ttk.Combobox(right_frame, textvariable=chosen_comic, state="readonly",
                              font=("Ariel", "12"),
                              width=20)
comic_combobox['values'] = comic_names
comic_combobox.grid(row=2, column=1, columnspan=1, padx=10, pady=10, sticky="WE")

# Entry Amount label - (row 3, column 0)
amount_label = Label(right_frame,
                        text="Amount:",
                        font=("Ariel", "12", "bold"),
                        bg=accent_color,
                        padx=10, pady=2
                        )
amount_label.grid(row=3, column=0, columnspan=1, padx=10, pady=5, sticky="WE")

# Comic Entry - (row 3, column 1)
# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = Entry(right_frame, textvariable=amount,
                     font=("Ariel", "12"), width=7
                     )
amount_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="W")

# Create a Button to sell a single chosen comic - (row 4, column 0)
sell_button = Button(right_frame, textvariable=chosen_mode,
                              font=("Ariel", "12"),
                              width=20, command=printy
                     )
sell_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main window loop
root.mainloop()
