from tkinter import *
win=Tk()
win.title("order app")
win.geometry("400x400")



fram=Frame(win,bg="lightblue")
fram.pack(fill=BOTH,expand=True,padx=40,pady=10)

labelmain=Label(fram,text="MENU",bg="lightblue")
labelmain.pack(pady=5,padx=5)

label1=Label(fram,text="burger: 3 usd ",bg="lightblue")
label1.place(x=10,y=50)

entry1=Entry(fram)
entry1.place(x=200,y=55)

label2=Label(fram,text="fries: 2 usd ",bg="lightblue")
label2.place(x=10,y=100)

entry2=Entry(fram)
entry2.place(x=200,y=105)


label3=Label(fram,text="pizza: 3 usd ",bg="lightblue")
label3.place(x=10,y=150)

entry3=Entry(fram)
entry3.place(x=200,y=155)


label4=Label(fram,text="cola: 1 usd ",bg="lightblue")
label4.place(x=10,y=200)

entry4=Entry(fram)
entry4.place(x=200,y=205)


label5=Label(fram,text="water: 50.5 usd ",bg="lightblue")
label5.place(x=10,y=250)

entry5=Entry(fram)
entry5.place(x=200,y=255)


def ordertake():
    la1=int(entry1.get())
    la2=int(entry2.get())
    la3=int(entry3.get())
    la4=int(entry4.get())
    la5=int(entry5.get())
    sum=float((la1*3)+(la2*2)+(la3*3)+(la4*1)+(la5/2))
    labelsum=Label(fram,bg="lightblue",text=f"total: {sum}")
    labelsum.place(x=150,y=330)


butto=Button(fram,text="take order",command=ordertake)
butto.place(x=150,y=300)


win.mainloop()






"""
from tkinter import *

from tkinter import ttk

win = Tk()

win.title("Restaurant Management System")

win.geometry("700x500")

currencyVar = StringVar()

mainFrame = Frame(win, bg="lightblue")

mainFrame.pack(fill=BOTH, expand=1,padx=40, pady=40)

dictonarySymbol ={

"USD":"$",

"Rupees":"₹",

"Euros":"€",

"Krone": "kr"

}

def currencyValueConverter(currency,total):

if currency == "USD":

return total

elif currency == "Rupees":

return total * 82

elif currency == "Euros":

return total * 0.95

elif currency == "Krone":

return total * 10.25

def calculateOrder():

firedMeal = int(friedMealEntry.get())

burger = int(burgerEntry.get())

total = firedMeal * 2 + burger * 3

currency = currencyVar.get()

Updatedtotal = currencyValueConverter(currency,total)

totalLabel = Label(mainFrame, text="Total: " + str(Updatedtotal) + dictonarySymbol[currency], font=("Arial", 15), bg="lightblue")

totalLabel.place(x=150, y=250)

mainLabel = Label(mainFrame, text="Restaurant Management System", font=("Arial", 20), bg="lightblue")

mainLabel.pack()

firedMeal = Label(mainFrame, text="Fired Meal(2$)", font=("Arial", 15), bg="lightblue")

firedMeal.place(x=10, y=50)

friedMealEntry = Entry(mainFrame)

friedMealEntry.place(x=200, y=55)

burger = Label(mainFrame, text="Burger(3$)", font=("Arial", 15), bg="lightblue")

burger.place(x=10, y=100)

burgerEntry = Entry(mainFrame)

burgerEntry.place(x=200, y=105)

currency = Label(mainFrame, text="Currency", font=("Arial", 15), bg="lightblue")

currency.place(x=10, y=150)

dropDown = ttk.Combobox(mainFrame,values=["USD","Rupees","Euros","Krone"] ,textvariable=currencyVar,width=10)

dropDown.place(x=150, y=150)

dropDown.set("USD")

placeButton = Button(mainFrame, text="Place Order", font=("Arial", 15), bg="lightgreen",command=calculateOrder)

placeButton.place(x=150, y=200)

win.mainloop()

"""
