from tkinter import *

window=Tk()
#use Tk class to create window object, which is what you will embedd widgets to
def km_to_miles():
    miles = int(e1_value.get()) * 1.6
    t1.insert(END, miles)

b1=Button(window,text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)
#entry is an input field

t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)
#text is an output field

window.mainloop()