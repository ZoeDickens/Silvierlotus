import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import time
#import Tkinter as tk     # python
#import tkFont as tkfont  # python 2


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Prolog, exit, U1, U2, U3, prologuetext):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.geometry("500x500")
        # if (page_name == "prologuetext"):
        #     frame = self.frames[page_name]
        #     frame.tkraise()
        #     time.sleep(10)
        #     self.show_frame("Prolog")
        # else:
        #     frame = self.frames[page_name]
        #     frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "test2.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="Welcome to the order of the Silver Lotus ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Order of the Silver Lotus", font=controller.title_font)

        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Play",
                            command=lambda: self.show())
        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame("Exit"))
        button3 = tk.Button(self, text="Settings",
                            command=lambda: controller.show_frame("Settings"))
        button1.pack()
        button2.pack()
        button3.pack()


        button1.config( height = 1, width = 15, pady = 30)
        button2.config( height = 1, width = 9, pady = 30)
        button3.config( height = 1, width = 8, pady = 30)


    def show(self):
        #self.controller = controller
        self.controller.show_frame("prologuetext")
        self.controller.after(5000, self.controller.show_frame, "Prolog")




class Prolog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="first upgrade",command=lambda: controller.show_frame("U1"))
        button2 = tk.Button(self, text="second upgrade",command=lambda: controller.show_frame("U2"))
        button3 = tk.Button(self, text="third upgrade",command=lambda: controller.show_frame("U3"))
        button.pack()
        button2.pack()
        button3.pack()

class prologuetext(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Prologue Begins", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Sillatine, 2E 314", font=controller.title_font)
        label.pack(side="top", fill="x", pady=15)
        label = tk.Label(self, text="Verenia’s Workshop", font=controller.title_font)
        label.pack(side="top", fill="x", pady=20)






class U1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the upgrade page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class U2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is upgrade 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=20)


class U3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is upgrade 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=30)



class exit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        command=quit





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
