from tkinter import *
win=Tk()
win.title("main window")
win.geometry("400x400")


def calc():
    newin=Toplevel(win,bg="green")
    newin.title("calculator")
    newin.geometry("200x400")

calcbutto=Button(win,text="calculator application",command=calc)
calcbutto.grid(row=0,column=0,pady=10,padx=10)

def feedback():
    newin=Toplevel(win,bg="blue")
    newin.title("feedback")
    newin.geometry("200x200")

feedbackbutto=Button(win,text="feedback",command=feedback)
feedbackbutto.grid(row=0,column=2,padx=10,pady=10)

def downloadyoutube():
    newin=Toplevel(win,bg="red")
    newin.title("download from youtube")
    newin.geometry("200x150")

youtubedownloadbutto=Button(win,text="download from Youtube",command=downloadyoutube)
youtubedownloadbutto.grid(row=1,column=1,padx=10,pady=10)

win.mainloop()
