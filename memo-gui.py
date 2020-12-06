import os
from tkinter import *

root = Tk()
root.title("Notes")
root.geometry("640x480")


filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_format = Menu(menu, tearoff=0)
menu_edit = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_window = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)

menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Close", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

menu.add_cascade(label="Format", menu=menu_format)
menu.add_cascade(label="Edit", menu=menu_edit)
menu.add_cascade(label="View", menu=menu_view)
menu.add_cascade(label="Window", menu=menu_window)
menu.add_cascade(label="Help", menu=menu_help)


root.config(menu=menu)
# scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Writing Area
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.mainloop()
