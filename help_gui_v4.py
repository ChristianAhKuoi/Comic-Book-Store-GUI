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

    # If user presses cross at top right, closes help and 'releases' help button
    help_box.protocol('WM_DELETE_WINDOW', close_help)
        
    # Help frame
    help_frame = ttk.Frame(help_box, width=300, height=300)
    help_frame.grid(row=0, column=0)

    # Help label - Heading (row 0, column 0)
    help_label_1 = ttk.Label(help_frame,
                            text="Help / Instructions",
                            font=("Ariel", "16", "bold"),
                            )
    help_label_1.grid(row=0, column=0)

    # Help label - Text (row 1, column 0)
    help_label_2 = ttk.Label(help_frame,
                            text="Some random help text.",
                            font=("Ariel", "12"),
                            )
    help_label_2.grid(row=1, column=0)

    # Help button (row 2, column 0)
    dismiss_button = ttk.Button(help_frame,
                                text = "Close",
                                command=close_help
                                )
    dismiss_button.grid(row=2, column=0)    

##########   FUNCTION AND SETUP - COMIC WINDOW   ##########
# Opens the help window when help button is pressed

   
           

##########   COMIC GUI CODE   ##########
# Create a window with a title
root = Tk()
root.title("Comic Book Store")

# Comic frame
comic_frame = ttk.Frame(root, width=300, height=300)
comic_frame.grid(row=0, column=0)

# Comic label - Heading (row 0, column 0)
comic_label = ttk.Label(comic_frame,
                        text="Comic Book Store",
                        font=("Ariel", "16", "bold")
                        )
comic_label.grid(row=0, column=0)

# Help button (row 1, column 0)
help_button = ttk.Button(comic_frame,
                         text = "Help",
                         command=help
                         )
help_button.grid(row=1, column=0)

# Run the main window loop
root.mainloop()
