import requests
from tkinter import *

win=Tk()
win.title("weather application")
win.geometry("400x400")

url = "https://api.openweathermap.org/data/2.5/weather"
api= "4a12c4e95662ce85e5cb1d0bc2945e2e"


def getweather():
    city=entry.get().strip()
    if not city:
        fram.config(text="please enter a city name")
        return
    params={"q":city,"appid":api,"units":"metric"}
    res=requests.get(url,params=params,timeout=8)
    data=res.json()
    print(data)
    datasring= str(data["main"]["temp"]) +"degrees celcius"+ "\n" +"it feels like "+ str(data["main"]["feels_like"]) +"\n"+"wind speed is: "+ str(data["wind"]["speed"])
    fram.config(text=datasring)

entry=Entry(win)
entry.place(x=140,y=50)

butto=Button(win,text="get the weather",bg="blue",command=getweather)
butto.place(x=150,y=100,)

fram=Label(win)
fram.place(x=135,y=150)

win.mainloop()
