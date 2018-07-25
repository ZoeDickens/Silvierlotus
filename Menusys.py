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
        # print ("Welcome,,\n 1. print Hello \n 2. print world \n 3. print python \n  4. print Hello world,welcome to my program")
        # choices = input()
        #
        # if choices == "1":
        #     print("PLAY")
        #     menu()
        #
        # if choices == "2"
        #     print ("Exit")
        #     menu()
        #
        # if choices == "3"
        #     print ()
        #     menu()
        #
        # if choices == "4"
        #     print ("")
        #     menu()

menu()
