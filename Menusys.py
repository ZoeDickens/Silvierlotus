from tkinter import *
def menu ():
    root  = Tk()
    root.geometry("1200x2200")
    mb = Menubutton(root, text = "This is a menu")
    mb.menu = Menu(mb)
    mb["menu"] = mb.menu
    mb.menu.add_command(label = "Play", command = lambda:[print("this is play")])
    mb.menu.add_command(label = "Exit", command = lambda: [print("this is Exit")])
    mb.pack()
    root.mainloop()

menu()


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
