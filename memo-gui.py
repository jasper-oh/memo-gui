from tkinter import *

root = Tk()
root.title("Notes")
root.geometry("640x480")


def open():
    pass


def save():
    pass


menu = Menu(root)
menu_file = Menu(menu, tearoff=0)

menu_file.add_command(label="Open", command=open)
menu_file.add_command(label="Save", command=save)
menu_file.add_separator()
menu_file.add_command(label="Close", command=root.quit)

menu_file.add_cascade(label="File", menu=menu_file)

menu.add_cascade(label="Format")
menu.add_cascade(label="Edit")
menu.add_cascade(label="View")
menu.add_cascade(label="Window")
menu.add_cascade(label="Help")


root.config(menu=menu)
root.mainloop()
