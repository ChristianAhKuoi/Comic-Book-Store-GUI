##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   CLASS CODE   ##########
class Comic:
    """This code will store the details of each comic (Super Dude, Lizard Man, Water Woman)"""
    def __init__(self, title, stock):
        self.title = title
        self.stock = stock
        
##########   FUNCTION AND SETUP   ##########
# Opens the help window when help button is pressed
def help():
    print("Help button feedback")
    
    ##########   HELP GUI CODE   ##########
    # Create a help window with a title
    help_box = Toplevel()
    help_box.title("Comic Book Store Help")
    
    # Help frame
    help_frame = ttk.Frame(help_box, width=300, height=300)
    help_frame.grid(row=0, column=0)

    # Help label - Heading (row 0, column 0)
    help_label = ttk.Label(help_frame,
                            text="Help",
                            font=("Ariel", "16", "bold")
                            )
    help_label.grid(row=0, column=0)

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
