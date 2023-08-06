#bigtin 8/6/23 v0.02

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
def input_factor():
    factor_input = entry.get()
    print("INPUT:", factor_input)


entry = ttk.Entry(frm)
entry.grid(column=0,row=3)
ttk.Button(frm, text="GO!", command=input_factor).grid(column=0,row=2)




#not sure what this but its very important :O
root.mainloop()