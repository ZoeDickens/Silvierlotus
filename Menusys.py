
from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont 
# from tkinter import tk, Font, Label

# class Window(Frame):


def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    self.init_window()

#Creation of init_window

#size of the window

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # self.title_font = tk.font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (startPage, firstPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("startPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # changing the title of our master widget
        # self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        #self.pack(fill=BOTH, expand=1)

        # creating a button instance
        playButton = Button(self, text="Play", height = 0, width = 10, command = lambda: controller.show_frame("firstPage"))

        # placing the button on my window
        playButton.place(x=700, y=450)
        playButton.pack()

        # changing the title of our master widget
        controller.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        #ExitButton = Button(self, text="Exit", height = 0, width = 10, command = goodbye.closeScreen())

        # placing the button on my window
        #ExitButton.place(x=700, y=500)

class firstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the first page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class goodbye(tk.Frame):
    def closeScreen():
        print("close") #dummy
        #Label(frame, text="this is a test").grid(row=1, column=1)

root = SampleApp()
# my_gui = startPage(root)
#
# root.geometry("2000x2000")

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




# import tkinter as tk                # python 3
# from tkinter import font  as tkfont # python 3
# #import Tkinter as tk     # python 2
# #import tkFont as tkfont  # python 2
#
# class SampleApp(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#
#         self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
#
#         # the container is where we'll stack a bunch of frames
#         # on top of each other, then the one we want visible
#         # will be raised above the others
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#         for F in (StartPage, PageOne, PageTwo):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame
#
#             # put all of the pages in the same location;
#             # the one on the top of the stacking order
#             # will be the one that is visible.
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame("StartPage")
#
#     def show_frame(self, page_name):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#
# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is the start page", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#
#         button1 = tk.Button(self, text="Go to Page One",
#                             command=lambda: controller.show_frame("PageOne"))
#         button2 = tk.Button(self, text="Go to Page Two",
#                             command=lambda: controller.show_frame("PageTwo"))
#         button1.pack()
#         button2.pack()
#
#
# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 1", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#
# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 2", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()
#
#
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()
