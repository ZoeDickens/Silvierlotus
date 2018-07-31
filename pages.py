import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3
import time
from random import randint

#import Tkinter as tk     # python
#import tkFont as tkfont  # python 2
# root = tk()
# T = Text(root, height=2, width=30)
# T.pack()
#

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")



        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Prolog, exit, U1, U2, U3, prologuetext, HOP, HOP2, HOP3, HOP4, bar, fight, end, percy, thanks, ignore, upgradesc):
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
        self.geometry("2000x2000")
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
        label = tk.Label(self, text="Order of the Silver Lotus", font=controller.title_font)

        label.pack(side="top", fill="x", pady = 15)

        button1 = tk.Button(self, text="Play",
                            command=lambda: self.show())
        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame("Exit"))
        button3 = tk.Button(self, text="Settings",
                            command=lambda: controller.show_frame("Settings"))

        button1.place(x=650, y=550)
        button2.place(x=650, y=590)
        button3.place(x=650, y=630)


        button1.config( height = 1, width = 13, pady = 15, padx = 25)
        button2.config( height = 1, width = 13, pady = 15, padx = 25)
        button3.config( height = 1, width = 13, pady = 15, padx = 25)
        button1.config(bg= "#d4d6d5")


    def show(self):
        #self.controller = controller
        self.controller.show_frame("prologuetext")
        self.controller.after(5000, self.controller.show_frame, "Prolog")



class percy(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        label = tk.Label(self, text=" 'Here are the upgrades you asked for, Doctor Charade,' he explained as he set the tray down on the already cluttered table beside her.\n"
        "The three tools on the tray rattled as they settled, the noise causing Verenia’s brows to furrow in annoyance.", font=controller.title_font)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label.pack(side="top", fill="x", pady=10)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Ignore",
                            command=lambda: controller.show_frame("ignore"))
        button2 = tk.Button(self, text="say thank you",
                            command=lambda: controller.show_frame("thanks"))
        button1.pack()
        button2.pack()


class thanks(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="'Thanks, Percy,' Verenia replied, placing the tools down to look closer at the objects settled on the tray. She didn’t watch her assistant as he left the room,\n"
        "his hands held tight behind his back in a strict manner.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="back to work",
                            command=lambda: controller.show_frame("upgradesc"))

        button1.pack()

class upgradesc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="She turned to the iron tray, her right hand reaching to pick up the first upgrade. \n"
        "It was a thin USB drive that looked very similar to the other two upgrades sitting upon the tray, yet it was colored in a red hue.\n"
        "The second upgrade was more yellow, while the third one was pink.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="All of these will affect how the HomeBot makes its choices. Red for resilience, yellow for compassion, and pink for humor.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Which upgrade will Verenia add that will affect how the HomeBot thinks?", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=10)








class Prolog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label.pack(side="top", fill="x", pady=1)

        button = tk.Button(self, text="Red (Resilience)",command=lambda: controller.show_frame("U1" ))
        button2 = tk.Button(self, text="Yellow (Compassion)",command=lambda: controller.show_frame("U2"))
        button3 = tk.Button(self, text="Pink (Humor)",command=lambda: controller.show_frame("U3"))
        button.pack()
        button2.pack()
        button3.pack()

class ignore(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="ignoring percy Verenia continued to work. Percy placed the tools down and walked out his hands held tight behind his back in a strict manner.\n"
        "She didn’t watch her assistant as he left the room", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="bakc to work",
                            command=lambda: controller.show_frame("upgradesc"))

        button1.pack()




class Prolog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        label = tk.Label(self, text="Midday’s light could be seen slipping through the humongous, glass windows on the left, yet Verenia couldn’t care less about the beauty of Sillatine.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Her hands were busy, thin tools in her hands moving through the wires of the disconnected HomeBot’s skull.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="She only stopped moving her hands and tilted her head back from her focus when the iron door opened, \n"
        "a tall man carrying a tray approaching her with a busy expression.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        button = tk.Button(self, text="look up",command=lambda: controller.show_frame("percy" ))
        button.config( height = 1, width = 13, pady = 1, padx = 1)
        button.pack()
        # label = tk.Label(self, text="'Thanks, Percy,' Verenia replied, placing the tools down to look closer at the objects settled on the tray. She didn’t watch her assistant as he left the room,\n"
        # "his hands held tight behind his back in a strict manner.", font=controller.title_font)
        # label.config(font=("Helvetica", 21))
        # label.pack(side="top", fill="x", pady=10)
        # label = tk.Label(self, text="She turned to the iron tray, her right hand reaching to pick up the first upgrade. \n"
        # "It was a thin USB drive that looked very similar to the other two upgrades sitting upon the tray, yet it was colored in a red hue.\n"
        # "The second upgrade was more yellow, while the third one was pink.", font=controller.title_font)
        # label.config(font=("Helvetica", 21))
        # label.pack(side="top", fill="x", pady=10)
        # label = tk.Label(self, text="All of these will affect how the HomeBot makes its choices. Red for resilience, yellow for compassion, and pink for humor.", font=controller.title_font)
        # label.config(font=("Helvetica", 21))
        # label.pack(side="top", fill="x", pady=10)
        # label = tk.Label(self, text="Which upgrade will Verenia add that will affect how the HomeBot thinks?", font=controller.title_font)
        # label.config(font=("Helvetica", 21))
        # label.pack(side="top", fill="x", pady=10)
        # button = tk.Button(self, text="look up",command=lambda: controller.show_frame("percy" ))
        # button2 = tk.Button(self, text="Yellow (Compassion)",command=lambda: controller.show_frame("U2"))
        # button3 = tk.Button(self, text="Pink (Humor)",command=lambda: controller.show_frame("U3"))
        # button.pack()
        # button2.pack()
        # button3.pack()




class prologuetext(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller = controller
        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="Prologue Begins", font=controller.title_font)
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Sillatine, 2E 314", font=controller.title_font)
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Verenia’s Workshop", font=controller.title_font)
        label.pack(side="top", fill="x", pady=2)






class U1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="After searching through each upgrade carefully, she selected her final choice.\n"
        "She picked up her tools again, moving the wires within the skull so she could inject the drive carefully.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="And by hearing the soft click, she knew the upgrade had been added", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Pushing some supplies away and enabling the upgrade through her old laptop, \n"
        "she moved to the ON switch in the corner of the room, her eyes wide with excitement.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Though, the moment she pulled the ON switch, a loud ringing bursted through her ears. \n"
        "Immense heat engulfed her before her senses vanished… following with her consciousness, as well.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        button = tk.Button(self, text="continue",command=lambda: self.show())
        button.pack()
    def show(self):
    #self.controller = controller
        self.controller.show_frame("HOP")
        self.controller.after(3000, self.controller.show_frame, "HOP2")
        self.controller.after(6000, self.controller.show_frame, "HOP3")
        self.controller.after(9000, self.controller.show_frame, "HOP4")


class U2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="After searching through each upgrade carefully, she selected her final choice.\n"
        "She picked up her tools again, moving the wires within the skull so she could inject the drive carefully.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="And by hearing the soft click, she knew the upgrade had been added", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Pushing some supplies away and enabling the upgrade through her old laptop, \n"
        "she moved to the ON switch in the corner of the room, her eyes wide with excitement.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Though, the moment she pulled the ON switch, a loud ringing bursted through her ears. \n"
        "Immense heat engulfed her before her senses vanished… following with her consciousness, as well.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        button = tk.Button(self, text="continue",command=lambda: self.show())
        button.pack()
    def show(self):
    #self.controller = controller
        self.controller.show_frame("HOP")
        self.controller.after(3000, self.controller.show_frame, "HOP2")
        self.controller.after(6000, self.controller.show_frame, "HOP3")
        self.controller.after(9000, self.controller.show_frame, "HOP4")

class U3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "lab3.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="After searching through each upgrade carefully, she selected her final choice.\n"
        "She picked up her tools again, moving the wires within the skull so she could inject the drive carefully.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="And by hearing the soft click, she knew the upgrade had been added", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Pushing some supplies away and enabling the upgrade through her old laptop, \n"
        "she moved to the ON switch in the corner of the room, her eyes wide with excitement.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="Though, the moment she pulled the ON switch, a loud ringing bursted through her ears. \n"
        "Immense heat engulfed her before her senses vanished… following with her consciousness, as well.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        button = tk.Button(self, text="continue",command=lambda: self.show())
        button.pack()
    def show(self):
    #self.controller = controller
        self.controller.show_frame("HOP")
        self.controller.after(3000, self.controller.show_frame, "HOP2")
        self.controller.after(6000, self.controller.show_frame, "HOP3")
        self.controller.after(9000, self.controller.show_frame, "HOP4")


class HOP(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="“Doctor Rylan.”", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

class HOP2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "doctor.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="“Yes?”", font=controller.title_font)
        label.pack(side="top", fill="x", pady=1)

class HOP3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_color= "black"
        label = tk.Label(self, text="“Take this. The Silver Lotus needs her back.”", font=controller.title_font)
        label.pack(side="top", fill="x", pady=1)

class HOP4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "doctor.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="......of course..I...I'll do it", font=controller.title_font)
        label.pack(side="top", fill="x", pady=1)
        lable = tk.Label(self, text="...", font=controller.title_font)
        lable = tk.Label(self, text="Prologue Ends", font=controller.title_font)
        button = tk.Button(self, text="continue",command=lambda:controller.show_frame("bar"))
        button.pack()
        button.place(x=650, y=550)

class exit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        command=quit


#combat stuff
class bar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background_image=tk.PhotoImage(file = "city.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = tk.Label(self, text="bar scene", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Mission one", font=controller.title_font)

        label.pack(side="top", fill="x", pady=1)



        label.pack(side="top", fill="x", pady=10)

class bar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Sillatine, 2E 315 The Winking Bot Bar", font=controller.title_font)

        label.pack(side="top", fill="x", pady=1)

        label.pack(side="top", fill="x", pady=10)

class bar(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        tk.Frame.__init__(self, parent

        label = tk.Label(self, text="The duo leaves the bar and enters the rain pouring upon the streets, only to be greeted by a woman with a prosthetic arm.",font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="She wore goggles upon her head, eyes wide in terror.", font=controller.title_font)
        label.config(font=("Helvetica", 21))
        label = tk.Label(self, text="“Help- you gotta help me!” she called, hands raised in front of her as if she was forming a shield for herself. \n"
        "Ariella turned to the woman, her brows arching. 'With what-'")

        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="She paused once she noticed two men donned in black approaching them from the front. Her veins froze in terror.")
        label.pack(side="top", fill="x", pady=10)

        label.pack(side="top", fill="x", pady=1)

        button = tk.Button(self, text="continue",command=lambda: self.show())
        button1 = tk.Button(self, text="Attack",command=lambda: controller.show_frame("fight"))

        button1.pack()
        button1.place(x=650, y=550)

class fight(tk.Frame):

    Ahealth = 200
    health = 100
    health_label = None
    Ahealth_lable = None
    Gaurds_lable = None
    Team_lable = None


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image=tk.PhotoImage(file = "city.gif")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self, text="fight scene", font=controller.title_font)
        label.pack(side="top", fill="x", pady=1)
        label = tk.Label(self, text="", font=controller.title_font)
        label.pack(side="top", fill="x", pady=1)
        self.health_label = tk.Label(self, text="health: 100", font=controller.title_font)
        self.health_label.pack(side="top", fill="x", pady=1)


        self.Ahealth_label = tk.Label(self, text="health: 200", font=controller.title_font)
        self.Ahealth_label.pack(side="top", fill="x", pady=1)

        button1 = tk.Button(self, text="shoot with gun", command=lambda: self.randomgen(1))
        button1.pack()
        button2 = tk.Button(self, text="punch", command=lambda: self.randomgen(2))
        button2.pack()
        button3 = tk.Button(self, text="heal", command=lambda: self.randomgen(3))
        button3.pack()

        self.Gaurds_lable = tk.Label(self, text="", font= self.controller.title_font)
        self.Gaurds_lable.pack(side="top", fill="x", pady=1)
        self.Team_lable = tk.Label(self, text="", font= self.controller.title_font)
        self.Team_lable.pack(side="top", fill="x", pady=1)


    def gun(self, stuff):
        if stuff == True:
            self.Ahealth -=10
            self.Ahealth_label.config(text = "health: " + str(self.Ahealth))
        else:
            self.health -=10
            self.health_label.config(text = "health: " + str(self.health))


    def punch(self, stuff):
        if stuff == True:
            self.Ahealth -=5
            self.Ahealth_label.config(text = "health: " + str(self.Ahealth))
        else:
            self.health -=5
            self.health_label.config(text = "health: " + str(self.health))

    def heal(self, stuff):
        if stuff == True:
            self.Ahealth +=10
            self.Ahealth_label.config(text = "health: " + str(self.Ahealth))
        else:
            self.health +=10
            self.health_label.config(text = "health: " + str(self.health))


    def randomgen(self, action):
        if self.health <= 0:
            self.controller.show_frame("end")
        else:
            if action == 1:
                self.gun(False)
                self.Team_lable.config(text="you shoot the guards and they lose health")
            elif action == 2:
                self.punch(False)
                self.Team_lable.config(text="you hit the guards and they lose health")
            elif action == 3:
                self.heal(False)
                self.Team_lable.config(text="you heal your team",)

            num = randint(1, 3)
            if num == 1 :

                self.gun(True)
                self.Gaurds_lable.config(text="the gaurds shoot you and you lose health",)
            elif num == 2:

                self.punch(True)
                self.Gaurds_lable.config( text="the gaurds hit you and you lose health")
            elif num == 3:

                self.heal(True)
                self.Gaurds_lable.config(self, text="The gaurds heal themselvs", font=self.controller.title_font)
                self.Gaurds_lable.pack(side="top", fill="x", pady=10)

class end(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="this is the end", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
