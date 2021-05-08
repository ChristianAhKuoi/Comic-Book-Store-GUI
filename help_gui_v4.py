##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   CLASS CODE   ##########
class Comic:
    """This code will store the details of each comic (Super Dude, Lizard Man, Water Woman)"""
    def __init__(self, title, stock):
        self.title = title
        self.stock = stock

##########   FUNCTION AND SETUP - HELP WINDOW   ##########
# Opens the help window when help button is pressed
def help():
    print("Help button feedback")
    # Disable help button
    help_button.config(state=DISABLED)

    # Close help window when 'close' button is pressed
    def close_help():
        help_button.config(state=NORMAL)
        help_box.destroy()
        print("Dismiss button feedback")

    ##########   HELP GUI CODE   ##########
    # Create a help window with a title
    help_box = Toplevel()
    help_box.title("Help / Instructions")

    # Set dimensions of help window
    help_box.geometry('350x300')

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
                            padx=30, pady=5
                            )
    help_label_1.grid(row=0, column=0, padx=10, pady=5)

    # Help label - Text (row 1, column 0)
    help_label_2 = Label(help_frame,
                            text="Some random help text. Some random help text. Some random help text. Some random help text. Some random help text. Some random help text. Some random help text. Some random help text. Some random help text. Some random help text.",
                            font=("Ariel", "11"),
                            wraplength=250,
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
root.configure(bg=tertiary_color)

# Comic frame
comic_frame = Frame(root, width=300, height=300, bg=tertiary_color)
comic_frame.grid(row=0, column=0, padx=20, pady=10)

# Comic label - Heading (row 0, column 0)
comic_label = Label(comic_frame,
                        text="Comic Book Store",
                        font=("Ariel", "16", "bold"),
                        bg=primary_color
                        )
comic_label.grid(row=0, column=0, padx=10, pady=5)

# Help button (row 1, column 0)
help_button = Button(comic_frame,
                         text = "Help",
                         font=("Ariel", "10", "bold"),
                         padx=10, pady=2,
                         command=help
                         )
help_button.grid(row=1, column=0, padx=10, pady=5)

# Run the main window loop
root.mainloop()
