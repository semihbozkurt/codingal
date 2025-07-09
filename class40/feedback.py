from tkinter import *
win=Tk()
win.title("feedback")
win.geometry("400x400")

def submitit():
    name=nameinput.get()
    email=mailinput.get()
    feedback=feedbackinput.get(1.0,END)

    print(name,email,feedback)

    dic={"name":name,
         "email":email,
         "feedback":feedback}

    file=open("feedback.txt","a")
    file.write(str(dic)+"\n")


username=Label(win,text="write your usere name")
username.grid(row=0,column=0,padx=10,pady=10)

nameinput=Entry(win)
nameinput.grid(row=0,column=1,padx=10,pady=10)

usermail=Label(win,text="write your mail")
usermail.grid(row=1,column=0,padx=10,pady=10)

mailinput=Entry(win)
mailinput.grid(row=1,column=1,padx=10,pady=10)

userfeedback=Label(win,text="feedback:")
userfeedback.grid(row=3,column=0,padx=10,pady=10)

feedbackinput=Text(win,height=5,width=15)
feedbackinput.grid(row=3,column=2,padx=10,pady=10)

submitbutton=Button(win,text="submit",command=submitit)
submitbutton.grid(row=4,column=2,pady=10)


win.mainloop()
