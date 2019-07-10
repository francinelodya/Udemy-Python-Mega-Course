from tkinter import *

window=Tk()

def kg_to_g():
    g = float(e1_value.get()) * 1000
    p = float(e1_value.get()) * 2.20462
    o = float(e1_value.get()) * 35.274
    t1.insert(END,g)
    t2.insert(END,p)
    t3.insert(END,o)


w0 = Label(window,text="Kg")
w0.grid(row=1,column=0)

w1 = Label(window,text="Grams")
w1.grid(row=2,column=0)

w2 = Label(window,text="Pounds")
w2.grid(row=2,column=1)

w3 = Label(window,text="Ounces")
w3.grid(row=2,column=2)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=1,column=1)

b1= Button(window,text="Convert",command=kg_to_g)
b1.grid(row=1,column=2)

t1 =Text(window,height=1,width=20)
t1.grid(row=3,column=0)

t2 =Text(window,height=1,width=20)
t2.grid(row=3,column=1)

t3 =Text(window,height=1,width=20)
t3.grid(row=3,column=2)

window.mainloop()
