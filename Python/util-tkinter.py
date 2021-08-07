#coding:utf-8

#by Lucky777

import os
from tkinter import *
from tkinter import messagebox, filedialog

#Configure window
def winConfig(window, title):
    xLeft = int(window.winfo_screenwidth()//2 - 1000)
    yTop = int(window.winfo_screenheight()//2 - 70)
    window.geometry(f"+{xLeft}+{yTop}")
    window.title(title)
    #img = PhotoImage(file=os.getcwd() + "/data/LuckyIcon.gif")
    window.tk.call("wm", "iconphoto", window._w, img)

#Button changes label text
def changeMsg(newText=""):
    msg.config(text=newText)
    win.update()

def info():
    messagebox.showinfo("Test", "This is an info!")
    changeMsg("You are informed")

def warn():
    messagebox.showwarning("Test", "This is a warning!")
    changeMsg("You are warned")

def askYN():
    if messagebox.askyesno("Test", "Are you sure?"):
        changeMsg("You said YES!")
    else:
        changeMsg("You said NO!")

def error():
    messagebox.showerror("Test", "There is an error!")
    changeMsg("There was an error!")

def selectFile():
    path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a file")
    changeMsg(f"You selected: {path}")

def dontCheckMe():
    if CB.get():
        if not messagebox.askyesno("Check box?", "Are you sure you want to check the box?"):
            CBDontCheck.deselect()
            changeMsg("Don't try again kid")
        else:
            changeMsg("Stupid.")
    else:
        changeMsg("You can quit now")

def selectLB():
    changeMsg(f"Item selected: {LB.get(ANCHOR)}")

#Button close window
def quit(window):
    if CB.get():
        messagebox.showerror("NOPE!", "Uncheck the box first... -_-")
    else:
        window.destroy()

#Main function
if __name__ == "__main__":
    win = Tk()
    global img
    img = PhotoImage(file=os.getcwd() + "/data/LuckyIcon.gif")
    winConfig(win, "Lucky Window")
    mainMenu = Menu(win)
    win.config(menu=mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New")
    fileMenu.add_separator()
    fileMenu.add_command(label="Quit", command=lambda: quit(win))
    CB = BooleanVar()

    #Creates widgets
    msg = Label(win, text="", width=50, height=3)
    frame = LabelFrame(win, text="This is a frame", width = 35, padx=5, pady=5)
    button = Button(frame, text="Lucky", command=lambda: changeMsg("Lucky world! :)"))
    button2 = Button(frame, text="nope", state=DISABLED)
    testsFrame = LabelFrame(win, text="Notice", padx=5, pady=5)
    buttonInfo = Button(testsFrame, text="Inform me", command=info)
    buttonWarn = Button(testsFrame, text="Warn me", command=warn)
    buttonAskYN = Button(testsFrame, text="Yes or no?", command=askYN)
    buttonError = Button(testsFrame, text="Error", command=error)
    buttonSelectFile = Button(win, text="Select a file", command=selectFile)
    CBDontCheck = Checkbutton(win, text="Don't check me!", variable=CB, command=dontCheckMe)
    buttonQuit = Button(win, text="QUIT", command=lambda: quit(win))

    LB = Listbox(win)
    tmpList=["First item", "Second item", "Third item"]
    for i in tmpList:
        LB.insert(END, i)

    buttonLB = Button(win, text="Select item", command=selectLB)

    status = Label(win, text="Nothing new..", bd=1, relief=SUNKEN, anchor=E)

    #Puts widgets in window
    msg.grid(row=0, column=0)

    frame.grid(row=1, column=0, padx=50, pady=25, sticky=N)
    button.grid(row=0, column=0)
    button2.grid(row=0, column=1)

    testsFrame.grid(row=2, column=0)
    buttonInfo.grid(row=0, column=0, padx=5, pady=10)
    buttonWarn.grid(row=0, column=1, padx=5, pady=10)
    buttonAskYN.grid(row=1, column=0, padx=5, pady=10)
    buttonError.grid(row=1, column=1, padx=5, pady=10)

    buttonSelectFile.grid(row=3, column=0, pady=25)

    CBDontCheck.grid(row=4, column=0, pady=10)

    buttonQuit.grid(row=5, column=0, pady=25)

    LB.grid(row=0, column=1)

    buttonLB.grid(row=1, column=1, pady=25)

    status.grid(row=6, column=0, sticky=W+E)

    #Loop window
    win.mainloop()