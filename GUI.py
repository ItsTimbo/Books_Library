from tkinter import *

root = Tk()

# frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# labels
headerLabel = Label(root, text="Welcome to your Digital Library")

# buttons
visualizeDataButton = Button(bottomFrame, text="Visualize Library", fg="black")
addISBNButton = Button(bottomFrame, text="Add ISBN", fg="black")

# packing
headerLabel.pack(fill=Y)
visualizeDataButton.pack(side=LEFT)
addISBNButton.pack()

root.mainloop()
