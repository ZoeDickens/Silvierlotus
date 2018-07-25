from tkinter import *
#import tkinter as Tk
#def menu ():

    root = Tk()
    root.geometry("1200x2200")
    import tkinter as Tk
    v=Tk.IntVar()
    command=lambda:print(v.get)
    radioButton1 =Radiobutton (root, variable = v, value = 0,text = "This is a menu")
    radioButton2 =Radiobutton (root, variable = v, value = 1,text = "This is a menu")
    radioButton1.pack()
    radioButton2.pack
    root.mainloop()

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
