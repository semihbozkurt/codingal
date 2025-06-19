from tkinter import *
win=Tk()
win.title("my first GUI")
win.geometry("500x500")

def buttonClick():
    print("button clicked")
    x=entry.get()
    text2.config(text=f"button is clicked by {x}")

text=Label(win,text="hello world",font=("Arial bold",20),bg="black",fg="white")
text.pack(pady=20)

entry=Entry(win,width=30)
entry.pack(pady=20)

butto=Button(win,text="click on me",font=("Arial bold",25),bg="red",fg="blue",command=buttonClick)
butto.pack(pady=20)



text2=Label(win,text="",font=("Arial bold",20),bg="black",fg="white")
text2.pack(pady=20)


win.mainloop()
