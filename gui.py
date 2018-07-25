
from tkinter import *

class App:
  def __init__(self, root):
    fm = Frame(root, width=2000, height=900, bg="gray")
    fm.pack(side=TOP, expand=NO, fill=NONE)



root = Tk()
display = App(root)
root.mainloop()
