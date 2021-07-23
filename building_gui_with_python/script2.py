from tkinter import *

window=Tk()

def kg_converter():
    kg = int(e1_value.get())
    t1.delete("1.0", END)
    t1.insert(END, str(kg * 1000) + " grams")
    t2.delete("1.0", END)
    t2.insert(END, str(kg * 2.20462) + " pounds")
    t3.delete("1.0", END)
    t3.insert(END, str(kg * 35.274) + " ounces")

b1=Button(window,text="Convert", command=kg_converter)
b1.grid(row=0, column=2)

e_label=Label(window, text="KG")
e_label.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)


t1=Text(window, height=1, width=15)
t1.grid(row=1, column=0)

t2=Text(window, height=1, width=15)
t2.grid(row=1, column=1)

t3=Text(window, height=1, width=15)
t3.grid(row=1, column=2)

window.mainloop()