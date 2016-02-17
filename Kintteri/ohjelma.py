__author__ = 'Ville'

import tkinter as tk

def tutorial_zero(root = tk.Tk):
    label = tk.Label(root, text="This is quite easy.")
    label.pack()
#
def tutorial_one(root = tk.Tk ):
    topFrame = tk.Frame(root)
    topFrame.pack()

    bottomFrame = tk.Frame(root)
    bottomFrame.pack(side=tk.BOTTOM)

    button1 = tk.Button(topFrame, text="Button 1", fg="red")
    button1.pack(side=tk.LEFT)
    button2 = tk.Button(topFrame, text="Button 2", fg="blue")
    button2.pack(side=tk.LEFT)
    button3 = tk.Button(topFrame, text="Button 3", fg="green")
    button3.pack(side=tk.LEFT)
    button4 = tk.Button(bottomFrame, text="Button 4", fg="purple")
    button4.pack(side=tk.BOTTOM)
#
def tutorial_two(root = tk.Tk):
    one = tk.Label(root, text="One", bg="red", fg="white")
    one.pack()
    two = tk.Label(root, text="Two", bg="green", fg="black")
    two.pack(fill=tk.X)
    three = tk.Label(root, text="Three", bg="blue", fg="white")
    three.pack(side=tk.LEFT, fill=tk.Y)
#
def tutorial_three(root = tk.Tk):
    label_1 = tk.Label(root, text="Name")
    label_2 = tk.Label(root, text="Password")

    entry_1 = tk.Entry(root)
    entry_2 = tk.Entry(root)

    label_1.grid(row=0, sticky=tk.E)
    label_2.grid(row=1, sticky=tk.E)

    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    chkbtn = tk.Checkbutton(root, text="Keep me logged in.")
    chkbtn.grid(columnspan=2)
#
def printName(event ):
    print("Hello, my name is Faggot!")
#
def tutorial_four(root = tk.Tk):
    button_1 = tk.Button(root, text="Print my name.")
    button_1.bind("<Button-1>", printName)
    button_1.pack()
#
def leftClick(event):
    print("Left")
#
def middleClick(event):
    print("Middle")
#
def rightClick(event):
    print("Right")
#
def tutorial_five(root= tk.Tk):
    frame = tk.Frame(root, width=800, height=600)
    frame.bind("<Button-1>", leftClick)
    frame.bind("<Button-2>", middleClick)
    frame.bind("<Button-3>", rightClick)

    frame.pack()
#
class BuckysButtons():

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.printButton = tk.Button(frame, text="Print message.", command=self.printMessage)
        self.printButton.pack(side=tk.LEFT)

        self.quitButton =  tk.Button(frame, text="Quit.", command=frame.quit)
        self.quitButton.pack(side=tk.LEFT)

    def printMessage(self):
        print("Wow, this actually worked!")
#
def tutorial_six(root = tk.Tk):
    b = BuckysButtons(root)
#
def doNothing():
    print("Ok ok, I won't...")
#
def tutorial_seven(root = tk.Tk):
    menu = tk.Menu(root)
    root.config(menu=menu)

    subMenu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Project...", command=doNothing)
    subMenu.add_command(label="New...", command=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=doNothing)

    editMenu = tk.Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=doNothing)
#
def tutorial_eight(root = tk.Tk):
    #   *****   Main menu   ******

    menu = tk.Menu(root)
    root.config(menu=menu)

    subMenu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Project...", command=doNothing)
    subMenu.add_command(label="New...", command=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=doNothing)

    editMenu = tk.Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=doNothing)

#   ****    Toolbar     *******
    toolbar = tk.Frame(root, bg="blue")

    insertButt = tk.Button(toolbar, text="Insert image", command=doNothing)
    insertButt.pack(side=tk.LEFT, padx=2, pady=2)
    printButt = tk.Button(toolbar, text="Print", command=doNothing)
    printButt.pack(side=tk.LEFT, padx=2, pady=2)

    toolbar.pack(side=tk.TOP, fill=tk.X)
#
def tutorial_nine(root = tk.Tk):
    #   *****   Main menu   ******

    menu = tk.Menu(root)
    root.config(menu=menu)

    subMenu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Project...", command=doNothing)
    subMenu.add_command(label="New...", command=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=doNothing)

    editMenu = tk.Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=doNothing)

#   ****    Toolbar     *******
    toolbar = tk.Frame(root, bg="blue")

    insertButt = tk.Button(toolbar, text="Insert image", command=doNothing)
    insertButt.pack(side=tk.LEFT, padx=2, pady=2)
    printButt = tk.Button(toolbar, text="Print", command=doNothing)
    printButt.pack(side=tk.LEFT, padx=2, pady=2)

    toolbar.pack(side=tk.TOP, fill=tk.X)

#   ******  Status Bar  ********
    status = tk.Label(root, text="Preparing to do nothing...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)
#
def main():
    root = tk.Tk()



    root.mainloop()
#
main()