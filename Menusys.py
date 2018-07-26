
from tkinter import *

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        playButton = Button(self, text="Play")

        # placing the button on my window
        playButton.place(x=700, y=450)


        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        ExitButton = Button(self, text="Exit")

        # placing the button on my window
        ExitButton.place(x=700, y=500)

root = Tk()

#size of the window
root.geometry("2000x2000")

app = Window(root)
root.mainloop()






















    # root = Tk()
    # root.geometry("1200x2200")
    # import tkinter as Tk
    # v=Tk.IntVar()
    # command=lambda:print(v.get)
    # radioButton1 =Radiobutton (root, variable = v, value = 0,text = "This is a menu")
    # radioButton2 =Radiobutton (root, variable = v, value = 1,text = "This is a menu")
    # radioButton1.pack()
    # radioButton2.pack
    # root.mainloop()

#menu()


# from tkinter import *
#
# root = Tk()
#
# import Tkinter as tk       #Import Tkinter
# root = tk.Tk()               #Bind Tkinter to the root object
# root.geometry("800x600")             #Set the window dimensions
# root.bind('<KeyPress>', onKeyPress)       #For example, bind the onKeyPress method (you must create it), and have some code
#                                                                        #done when key is pressed
# root.mainloop()         #Starts the Tkinter and onKeyPress event
