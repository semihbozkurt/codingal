# import requests
from tkinter import *

win=Tk()
win.title("weather application")
win.geometry("400x400")

def get():
    pass

entry=Entry(win)
entry.place(x=140,y=50)

butto=Button(win,text="get the weather",bg="blue",command=get)
butto.place(x=150,y=100,)

fram=Frame(win,height=150,width=150,bg="red")
fram.place(x=125,y=150)

win.mainloop()
