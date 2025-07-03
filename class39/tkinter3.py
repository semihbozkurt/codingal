from tkinter import *
from tkinter import messagebox as messageBox

win=Tk()
win.geometry("400x400")
win.title("mouse buttons")

frame=Frame(win,bg="red",height=50,width=50)
frame.place(x=0,y=0)

def f1(event):
    print("left")

def f2(event):
    print("middle")

def f3(event):
    ask=messageBox.askquestion("right","are you semih?")
    print("right")
    if ask=="yes": print("yes")

def f4(event):
    messageBox.showinfo("double click info","hello hello")
    print("double left")

#mouse buttons
win.bind("<Button-1>",f1)
win.bind("<Button-2>",f2)
win.bind("<Button-3>",f3)
win.bind("<Double-Button-1>",f4)


label=Label(win,text="click on a key")
label.pack(padx=5)
def f5(event):
    label.config(text=f"{event.char} key is pressed")

win.bind("<Key>",f5)

label2=Label(win,text="hi")
label2.pack(padx=5)

label3=Label(win,text="hi")
label3.pack(padx=5)

def mousemotion(event):
    label2.config(text=f"x: {event.x}  y: {event.y}")
    
    if 38>=event.x>=0 and 32>=event.y>=0:
        label3.config(text="red",bg="red")
        

    else:
        label3.config(text="white",bg="white")
        


win.bind("<Motion>",mousemotion)
win.mainloop()
