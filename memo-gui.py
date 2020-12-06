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
menu_format = Menu(menu, tearoff=0)
menu_edit = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_window = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)

menu_file.add_command(label="Open", command=open)
menu_file.add_command(label="Save", command=save)
menu_file.add_separator()
menu_file.add_command(label="Close", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

menu.add_cascade(label="Format", menu=menu_format)
menu.add_cascade(label="Edit", menu=menu_edit)
menu.add_cascade(label="View", menu=menu_view)
menu.add_cascade(label="Window", menu=menu_window)
menu.add_cascade(label="Help", menu=menu_help)


root.config(menu=menu)
root.mainloop()
