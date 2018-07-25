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
        playButton.place(x=, y=0)

root = Tk()

#size of the window
root.geometry("x300")

app = Window(root)
root.mainloop()
