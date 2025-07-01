from tkinter import *
win=Tk()
win.title("pad ")
win.geometry("400x400")

numlist=[[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]

for row in range(4):
    win.columnconfigure(row,weight=1,minsize=75)
    win.rowconfigure(row,weight=1,minsize=50)
    for col in range(3):
        frame=Frame(
            win,
            relief="raised",
            borderwidth=1
        )
        
        frame.grid(row=row,column=col,padx=10,pady=10)
        label=Button(frame,text=numlist[row][col])
        label.pack(padx=10,pady=10)
        print(numlist[row][col])



win.mainloop()
