##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   CLASS CODE   ##########
class Comic:
    """This code will store the details of each comic (Super Dude, Lizard Man, Water Woman)"""
    def __init__(self, title, stock):
        self.title = title
        self.stock = stock

class Help:
    def __init__(self):
        # Disable help button
        help_button.config(state=DISABLED)
        
        ##########   HELP GUI CODE   ##########
        # Create a help window with a title
        self.help_box = Toplevel()
        self.help_box.title("Help / Instructions")
        
        # Help frame
        self.help_frame = ttk.Frame(self.help_box, width=300, height=300)
        self.help_frame.grid(row=0, column=0)

        # Help label - Heading (row 0, column 0)
        self.help_label_1 = ttk.Label(self.help_frame,
                                text="Help / Instructions",
                                font=("Ariel", "16", "bold"),
                                )
        self.help_label_1.grid(row=0, column=0)

        # Help label - Text (row 1, column 0)
        self.help_label_2 = ttk.Label(self.help_frame,
                                text="Some random help text.",
                                font=("Ariel", "12"),
                                )
        self.help_label_2.grid(row=1, column=0)

        # Help button (row 2, column 0)
        self.dismiss_button = ttk.Button(self.help_frame,
                                 text = "Close",
                                 command=self.close_help
                                 )
        self.dismiss_button.grid(row=2, column=0)        

    ##########   FUNCTION AND SETUP - HELP WINDOW   ##########
    # Close help window when 'close' button is pressed
    def close_help(self):
        help_button.config(state=NORMAL)
        self.help_box.destroy()
        print("Dismiss Help Window")

##########   FUNCTION AND SETUP - COMIC WINDOW   ##########
# Opens the help window when help button is pressed
def help():
    print("Help button feedback")
    get_help = Help()        

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
