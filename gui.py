#bigtin 8/6/23 v0.01

from tkinter import *
from tkinter import ttk
#window stuff
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

#the wigets
ttk.Label(frm, text="v0.01").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)

# user input 
ttk.Entry().grid(column=0,row=3)
ttk.Button(frm, text="GO!").grid(column=0,row=2)

#not sure what this but its very important :O
root.mainloop()