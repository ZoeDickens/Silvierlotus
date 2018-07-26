
from tkinter import *

root = Tk()
T = Text(root, height=2, width=30)
T.pack()


def U1():
    text= "hello"

def U2():
    text= "hi"

def U3():
    text= "hey"

        def main():
            frame = Tk()
            frame.geometry("480x360")

            Label(frame, text="this is a test").grid(row=1, column=1)
            display = Label(frame, text="before") # we need this Label as a variable!
            display.grid(row=2, column=1)

            def add(amount):
                display.configure(text="changed")

            Button(frame, text="U1", command=lambda: add(.1)).grid(row=3, column=1)
            Button(frame, text="U2", command=lambda: add(.2)).grid(row=4, column=1)
            Button(frame, text="U3", command=lambda: add(.5)).grid(row=5, column=1)
        main()
