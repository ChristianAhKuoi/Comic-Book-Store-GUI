##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk

##########   FUNCTION AND SETUP   ##########
# Opens the help window when help button is pressed
def help():
    print("Help button feedback")

##########   GUI CODE   ##########
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
