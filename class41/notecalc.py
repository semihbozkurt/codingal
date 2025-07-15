from tkinter import *
win=Tk()
win.title("note calculator")
win.geometry("400x400")




def start():
    newin=Toplevel(win)
    newin.title("note calculator")
    newin.geometry("400x400")
    
    label=Label(newin,text="write the amount")
    label.grid(row=0,column=0,padx=10,pady=10)

    enter=Entry(newin)
    enter.grid(row=0,column=1,padx=10,pady=10)

    

    def calculat():
        getentery=int(enter.get())
        num2000=getentery//2000
        num500=(getentery-(num2000*2000))//500
        num100=(getentery-(num2000*2000 + num500*500))//100

        twothousend=Label(newin,text=f"number of two thousends is: {num2000}")
        twothousend.grid(row=2,column=0,padx=5,pady=5)

        fivehundered=Label(newin,text=f"number of five hundereds is: {num500}")
        fivehundered.grid(row=3,pady=5)

        hundered=Label(newin,text=f"number of hundereds is: {num100}")
        hundered.grid(row=4,column=0,pady=5)
    
    buttocalc=Button(newin,text="calculate",command=calculat)
    buttocalc.grid(row=0,column=2,padx=10,pady=10)


startbutto=Button(win,text="lets get started",command=start)
startbutto.pack()




win.mainloop()
