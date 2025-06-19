from tkinter import *

win=Tk()
win.title("calculator")
win.geometry("500x500")

def add():
    x=int(entry.get())
    y=int(entry2.get())
    text2.config(text=f"{x} + {y} = {x+y}")

def minus():
    x=int(entry.get())
    y=int(entry2.get())
    text2.config(text=f"{x} - {y} = {x-y}")

def multi():
    x=int(entry.get())
    y=int(entry2.get())
    text2.config(text=f"{x} x {y} = {x*y}")

def divi():
    x=int(entry.get())
    y=int(entry2.get())
    text2.config(text=f"{x} / {y} = {x/y}")

text=Label(win,text="Enter the numbers",font=("Arial bold",20),bg="black",fg="white")
text.pack(pady=20)

entry=Entry(win,width=30)
entry.pack(pady=20)

entry2=Entry(win,width=30)
entry2.pack(pady=20)

butto=Button(win,text="pluss",font=("Arial bold",15),bg="red",fg="blue",command=add)
butto.pack(pady=20)

butto2=Button(win,text="minus",font=("Arial bold",15),bg="red",fg="blue",command=minus)
butto2.pack(pady=20)

butto3=Button(win,text="multiplication",font=("Arial bold",15),bg="red",fg="blue",command=multi)
butto3.pack(pady=20)

butto4=Button(win,text="divition",font=("Arial bold",15),bg="red",fg="blue",command=divi)
butto4.pack(pady=20)

text2=Label(win,text="",font=("Arial bold",15),bg="black",fg="white")
text2.pack(pady=20)


win.mainloop()
