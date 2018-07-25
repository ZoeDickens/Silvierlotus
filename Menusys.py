from tkinter import *
def menu ():
    root  = Tk()
    root.geometry("200x200")
    mb = Menubutton(root, text = "This is a menu")
    mb.menu = Menu(mb)
    mb["menu"] = mb.menu
    mb.menu.add_command(label = "Play", command = lambda:[print("this is play")])
    mb.menu.add_command(label = "Exit", command = lambda: [print("this is Exit")])
    mb.pack()
    root.mainloop()

menu()
