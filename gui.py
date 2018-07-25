from tkinter import *


def main():
    # This is where we define the menu and give option to play
    root  = Tk()
    root.geometry("200x200")
    mb = Menubutton(root, text = "This is a menu")
    mb.menu = Menu(mb)
    mb["menu"] = mb.menu
    mb.menu.add_command(label = "Play", command = lambda:[print("this is play")])
    mb.menu.add_command(label = "Exit", command = lambda: [print("this is Exit")])
    mb.pack()
    # end menu code
    root.mainloop()

if __name__ == "__main__":
    main()
