#coding:utf-8

#by Lucky777

import os
from tkinter import *

#Configure window
def winConfig(window, title):
    xLeft = int(window.winfo_screenwidth()//2 - 1000)
    yTop = int(window.winfo_screenheight()//2 - 70)
    window.geometry(f"+{xLeft}+{yTop}")
    window.title(title)
    #img = PhotoImage(file=os.getcwd() + "/data/LuckyIcon.gif")
    window.tk.call("wm", "iconphoto", window._w, img)

#Button changes label text
def myButton(newText="No text"):
    msg.config(text=newText)
    win.update()

def test1():
    test = Toplevel() #New window must be Toplevel() and not Tk()
    winConfig(test, "Radio Button test")

    langs = ["English", "Français", "Neederlands"]
    lang = StringVar()
    lang.set("English")

    RBFrame = LabelFrame(test, text="Lang", padx=5, pady=5)
    RBFrame.grid(padx=25, pady=25)
    for i in langs:
        Radiobutton(RBFrame, text=i, variable=lang, value=i, command=lambda: quit(test)).grid(row=langs.index(i), sticky=W)

    test.mainloop()

#Button close window
def quit(window):
    window.destroy()

#Main function
if __name__ == "__main__":
    win = Tk()
    global img
    img = PhotoImage(file=os.getcwd() + "/data/LuckyIcon.gif")
    winConfig(win, "Lucky Window")

    #Creates widgets
    msg = Label(win, text="THIS IS A TEXT", height=3)
    frame = LabelFrame(win, text="This is a frame", width = 35, padx=5, pady=5)
    button = Button(frame, text="HELLO", command=lambda: myButton("HELLO! :)"))
    button2 = Button(frame, text="nope", state=DISABLED)
    testsFrame = LabelFrame(win, text="Tests", padx=5, pady=5)
    buttonTest1 = Button(testsFrame, text="RadioButton", command=test1)
    buttonQuit = Button(win, text="QUIT", command=lambda: quit(win))
    status = Label(win, text="Nothing new..", bd=1, relief=SUNKEN, anchor=E)

    #Puts widgets in window
    msg.grid(row=0, column=0)
    frame.grid(row=1, column=0, padx=50, pady=25, sticky=N)
    button.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    testsFrame.grid(row=2, column=0)
    buttonTest1.grid(row=0, column=0)
    buttonQuit.grid(row=3, column=0, pady=25)
    status.grid(row=4, column=0, sticky=W+E)

    #Loop window
    win.mainloop()