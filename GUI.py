import tkinter as tk
from tkinter import *

root = Tk()

# settings
root.title("Digital Library")
root.maxsize(1000, 400)

# frames
headFrame = Frame(root)
headFrame.pack()
topFrame = Frame(root)
topFrame.pack(fill=BOTH)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# labels
headerLabel = Label(headFrame, text="Welcome to your Digital Library", bg="blue")
topLabel = Label(topFrame, text="test text", bg="red")
# buttons
visualizeDataButton = Button(bottomFrame, text="Visualize Library", fg="black")
addISBNButton = Button(bottomFrame, text="Add ISBN", fg="black")

# packing
headerLabel.pack(fill=Y)
topLabel.pack(fill=BOTH)
visualizeDataButton.pack(anchor=CENTER, side=LEFT, padx=5, pady=5, expand=True)
addISBNButton.pack(anchor=CENTER, padx=5, pady=5, expand=True)

root.mainloop()
