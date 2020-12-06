from tkinter import *

root = Tk()
root.title("Notes")
root.geometry("640x480")


# scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Writing Area
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.mainloop()
