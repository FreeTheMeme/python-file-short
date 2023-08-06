#bigtin 8/6/23 v0.03

from tkinter import *
from tkinter import ttk
#window stuff
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
#vars
i = 1
factor = 0
answer = 0
#the wigets
ttk.Label(frm, text="v0.03").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# user input and factoring
def input_factor():
    factor = int(entry.get())
    for i in range (1, factor):
        answer = factor / i
    
        if factor < factor/2:
            continue
        elif answer.is_integer():
            ttk.Label(frm, text=i).grid(column=0, row=i + 2)
            ttk.Label(frm, text=answer).grid(column=1, row=i + 2)
            print(i,':done')
    
        else:
            continue


entry = ttk.Entry(frm)
entry.grid(column=0,row=1)
ttk.Button(frm, text="GO!", command=input_factor).grid(column=2,row=0)




#not sure what this but its very important :O
root.mainloop()