from tkinter import *

win=Tk()
win.title("geometry")
win.geometry("400x400")

"""frame=Frame(win,bg="lightblue",padx=30,pady=30)
frame.pack(pady=20)

text=Label(frame,text="hello world")
text.pack(pady=10)

butto=Button(frame,text="click here")
butto.pack(pady=5)
"""
leftframe=Frame(win,bg="lightgreen",height=400,width=150)
leftframe.pack(side=LEFT,fill="both",expand=True)

rightframe=Frame(win,bg="lightyellow",height=400,width=250)
rightframe.pack(side=RIGHT,fill="both",expand=True)

menu=Button(leftframe,text="MENU",bg="red",fg="white",relief="solid")
menu.pack(padx=10,pady=10)

win.mainloop()
