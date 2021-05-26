##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   CLASS CODE   ##########
class Comic:
    """This code will store the details of each comic (Super Dude, Lizard Man, Water Woman)"""
    def __init__(self, name, stock, sold):
        self.name = name
        self.stock = int(stock)
        self.sold = int(sold)
        comic_list.append(self)

    # Sells a chosen comic
    def sell(self, amount):
        if amount <= self.stock:
            self.stock -= amount
            self.sold += amount
            return True
        else:
            return False

    # Restocks a set amount of the chosen comic
    def restock(self, amount):
        if amount > 0:
            self.stock += amount
            return True
        else:
            return False

##########   FUNCTION AND SETUP - COMIC WINDOW   ##########
# Reads the comic.txt for the instances of the comic class
def get_data():
    comic_file = open("comics.txt","r")
    line_list = comic_file.readlines()

    for line in line_list:
        comic_data = line.strip().split(",")
        Comic(*comic_data)

    comic_file.close()
    
# Creates a name list to store every comic name in
def create_name_list():
  name_list = []
  for comic in comic_list:
    name_list.append(comic.name)
  return name_list

# Creates a function that will update the summary
def update_summary():
    total_stock_sold = 0
    stock_string = ""
    stock_string += "List of Comics:\n\n"
    comic_file = open("comics.txt","w")

    # Append each comic's name, and stock to the summary label
    for comic in comic_list:
        stock_string += "{}: {}\n".format(comic.name, comic.stock)
        total_stock_sold += comic.sold
        comic_file.write("{},{},{}\n".format(comic.name, comic.stock, comic.sold))
        
    stock_string += "\nTotal Comics Sold: {}".format(total_stock_sold)
    comic_details.set(stock_string)
    comic_file.close()

# When sell radio button is pressed...
def mode_sell():
    # hide amount label and entry widgets
    amount_label.grid_remove()
    amount_entry.grid_remove()
    # set chosen_mode from mode_list to "Sell"
    chosen_mode.set(mode_list[0])

# When restock radio button is pressed...
def mode_restock():
    # show amount label and entry widgets
    amount_label.grid()
    amount_entry.grid()
    # set chosen_mode from mode_list to "Restock"
    chosen_mode.set(mode_list[1])
    # updates the amount to make the entry box blank
    amount.set("")

# Create a sell function
def sell_stock(comic):
    if comic.sell(amount.get()):
        action_feedback_label.config(fg="lime")
        action_feedback.set("Success! {} {} comics were sold.".format(amount.get(), comic.name))
    else:
        action_feedback_label.config(fg="red")
        action_feedback.set("Uh Oh! {} is out of stock.".format(comic.name))

# Create a sell function
def restock_stock(comic):
    try:
        if comic.restock(amount.get()):
            action_feedback_label.config(fg="lime")
            action_feedback.set("Success! {} {} comics were restocked.".format(amount.get(), comic.name))
        else:
            action_feedback_label.config(fg="red")
            action_feedback.set("Please enter a positive integer.".format(comic.name))
    except:
        action_feedback_label.config(fg="red")
        action_feedback.set("Please enter a number.".format(comic.name))

# When Sell/Restock Button is pressed...
def manage_stock():
    for comic in comic_list:
        if chosen_comic.get() == comic.name:
            if mode_var.get() == "sell":
                amount.set(1)
                sell_stock(comic)
            elif mode_var.get() == "restock":
                restock_stock(comic)
            else:
                pass
    # Update the Summary GUI 
    update_summary()
    amount.set("")

# Opens the help window when help button is pressed
def help():
    # Disable help button
    help_button.config(state=DISABLED)

    # Close help window when 'close' button is pressed
    def close_help():
        help_button.config(state=NORMAL)
        help_box.destroy()

    ##########   HELP GUI CODE   ##########
    # Create a help window with a title
    help_box = Toplevel()
    help_box.title("Help / Informations")

    # Set dimensions of help window
    help_box.geometry('400x350')

    # Set color of help window background
    help_box.configure(bg=tertiary_color)

    # Basically makes the frame centre to the middle of the window
    help_box.grid_columnconfigure(0, weight=1)

    # If user presses cross at top right, closes help and 'releases' help button
    help_box.protocol('WM_DELETE_WINDOW', close_help)
        
    # Help frame
    help_frame = Frame(help_box, width=350, height=400,
                       bg=tertiary_color, padx=20, pady=20
                       )
    help_frame.grid(row=0, column=0, sticky="NS")

    # Help label - Heading (row 0, column 0)
    help_label_1 = Label(help_frame,
                            text="Help / Information",
                            font=("Ariel", "16", "bold"),
                            bg=primary_color,
                            padx=40, pady=5
                            )
    help_label_1.grid(row=0, column=0, padx=10, pady=5)

    # Help label - Text (row 1, column 0)
    help_label_2 = Label(help_frame,
                            text="The left side of the program displays the details of the comics which include the comic's name, the comic's stock, and lastly the total comics that have been sold."
                                 "\nThe right side of the program is used to sell a single comic or to restock a set amount of comics."
                                 "\n\nWhen the sell mode is selected, hit button to sell a chosen comic using the dropdown menu."
                                 "\nWhen the restock mode is selected, enter a positive number in the entry field and hit the button to restock the chosen comic.",
                            font=("Ariel", "10"),
                            wraplength=300,
                            justify="center",
                            bg=accent_color,
                            padx=10, pady=10
                            )
    help_label_2.grid(row=1, column=0, padx=10, pady=5)

    # Help button (row 2, column 0)
    dismiss_button = Button(help_frame,
                                text = "Close",
                                font=("Ariel", "10", "bold"),
                                padx=10, pady=2,
                                command=close_help
                                )
    dismiss_button.grid(row=2, column=0, padx=10, pady=5)    

# Formatting Variables...
primary_color = "#38c8f5" #sky blue
secondary_color = "#e31679" #deep pink
tertiary_color = "#242424" #light black
accent_color = "#a6e5d0" #pale blue

# Setup Lists
comic_list = []
mode_list = ['Sell', 'Restock']

# Creating instances of comic class
get_data()
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

# Top frame (row 0, column 0)
top_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

# Comic label - Heading (row 0, column 0)
comic_label = Label(top_frame,
                        text="Comic Book Store",
                        font=("Ariel", "16", "bold"),
                        bg=primary_color,
                        padx=240, pady=5, anchor="center"
                        )
comic_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="N")

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
update_summary()

# Stock Details label - (row 1, column 0)
details_label = Label(left_frame, textvariable=comic_details,
                      font=("Ariel", "12", "bold"),
                      bg=accent_color, padx=10, pady=5
                      )
details_label.grid(row=1, column=0, columnspan=1, padx=10, pady=10)

# Right frame (row 1, column 1)
right_frame = Frame(comic_frame, width=300, height=250, bg=tertiary_color)
right_frame.grid(row=1, column=1, padx=10, pady=5, sticky="NS")

# Stock Manager label - (row 0, column 0)
mode_label = Label(right_frame,
                        text="Stock Manager",
                        font=("Ariel", "16", "bold"),
                        width=22,
                        bg=secondary_color,
                        padx=10, pady=5
                        )
mode_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

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
                             value="sell", variable=mode_var,
                             command=lambda: mode_sell()
                              )
sell_radio.grid(row=0, column=0, padx=10, pady=2)

# Restock Radiobutton (row 0, column 1)
restock_radio = ttk.Radiobutton(mode_label_frame, text="Restock",
                                value="restock", variable=mode_var,
                                command=lambda: mode_restock()
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
                        padx=5, pady=2
                        )
amount_label.grid(row=3, column=0, columnspan=1, padx=10, pady=5, sticky="WE")
amount_label.grid_remove()

# Comic Entry - (row 3, column 1)
# Create a variable to store the amount
amount = IntVar()
amount.set("")

# Create an entry to type in amount
amount_entry = Entry(right_frame, textvariable=amount,
                     font=("Ariel", "12"), width=7
                     )
amount_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="W")
amount_entry.grid_remove()

# Help button (row 4, column 0)
help_button = Button(right_frame,
                         text = "Help",
                         font=("Ariel", "12"),
                         padx=10,
                         command=help
                         )
help_button.grid(row=4, column=0, padx=10, pady=10)

# Button text variable
chosen_mode = StringVar()
chosen_mode.set(mode_list[0])

# Create a Button to sell or restock comics - (row 4, column 1)
manage_stock_button = Button(right_frame, textvariable=chosen_mode,
                              font=("Ariel", "12"),
                              width=20, command=manage_stock
                     )
manage_stock_button.grid(row=4, column=1, columnspan=1, padx=10, pady=10)

# Create an action feedback label - (row 4, column 0)
action_feedback = StringVar()
action_feedback.set("Welcome!")
action_feedback_label = Label(right_frame, textvariable=action_feedback,
                              font=("Ariel", "12"),
                              bg=tertiary_color, fg="white",
                              wrap=290,
                              padx=5, pady=2
                              )
action_feedback_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the main window loop
root.mainloop()
