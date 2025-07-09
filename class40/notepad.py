from tkinter import *
from tkinter import messagebox
import os
win = Tk()
win.title("notepad")
win.geometry("500x500")

def createNewFile():
    textArea.delete(1.0,END)

def openFile():
    win3=Toplevel(win)
    win3.title("file list")
    win3.geometry("200x200")
    filelist=Listbox(win3)
    filelist.pack(fill=BOTH,expand=True)

    files=os.listdir("notepadfiles")
    for file in files:
        filelist.insert(END,file)


    def choseFile(event):
        choice=filelist.get(filelist.curselection()[0])

        with open(f"notepadfiles/{choice}","r",encoding="utf-8") as f:
            inside=f.read()
            textArea.delete(1.0,END)
            textArea.insert(END,inside)
        win3.destroy()
    
    filelist.bind("<Double-Button-1>",choseFile)

def saveFile():

    win2= Toplevel()
    win2.title("save file")
    win2.geometry("150x150")

    writename=Label(win2,text="name of the file:")
    writename.grid(row=0,column=0,pady=10)

    filename=Entry(win2)
    filename.grid(row=1,column=0,pady=10)

    

    def save():
        fileName=filename.get()
        if not fileName.strip():
            messagebox.showwarning("warning","file name can not be empty")
            return
        
        with open(f"notepadfiles/{fileName}","w",encoding="utf-8") as file:
            text=textArea.get(1.0,END)
            file.write(text.strip())
        win2.destroy()

    savebutton=Button(win2,text="save",command=save)
    savebutton.grid(row=2,column=0)
        



textArea = Text(win)
textArea.pack(fill=BOTH,expand=True)

menu = Menu(win)
win.config(menu=menu)
fileMenu = Menu(menu,tearoff=1)
menu.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="New",command=createNewFile)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)

win.mainloop()
